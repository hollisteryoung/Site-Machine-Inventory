import re 
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
import networkx as nx
from pyvis.network import Network

file = 'Chris_AC13/_04_BAR_PNC_Program.L5X'
current_dir = 'Chris_AC13'
files = [f for f in listdir(current_dir) if isfile(join('Chris_AC13', f))]



token_specification = [
    ('NUMBER', r'-?\d+\.?\d*'),
    ('QMARK',  r'\?'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACK', r'\['),
    ('RBRACK', r'\]'),
    ('COMMA',  r','),
    ('SEMI',   r';'),
    ('WORD',   r'[A-Za-z_][A-Za-z0-9_:.]*'),
    ('SKIP',   r'[ \t]+'),
    ('MISMATCH', r'.'),
]
tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

tree = ET.parse(file)
root = tree.getroot()

def tag_calls(rung_text):
    tokens = list(re.finditer(tok_regex, rung_text))
    tokens = [t for t in tokens if t.lastgroup != 'SKIP']

    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.lastgroup == 'WORD' and i + 1 < len(tokens) and tokens[i+1].lastgroup == 'LPAREN':
            name = t.group()
            depth = 1
            j = i + 2
            operand_start = tokens[j].start()
            operands = []
            while depth:
                k = tokens[j].lastgroup
                if k == 'LPAREN':
                    depth += 1
                elif k == 'RPAREN':
                    depth -= 1
                    if depth == 0:
                        operands.append(rung_text[operand_start:tokens[j].start()].strip())
                elif k == 'COMMA' and depth == 1:
                    operands.append(rung_text[operand_start:tokens[j].start()].strip())
                    operand_start = tokens[j].end()
                j += 1
            yield name, [o for o in operands if o]
            i = j
        else:
            i += 1

NOT_A_TAG = {
    'Disabled', 'Enabled', 'Programmed', 'Immediate', 'None', 'All', 'No', 'Yes',
    'Absolute', 'Actual', 'Trapezoidal', 'S-Curve', 'Positive', 'Negative',
}         
WRITES = {
    'OTE': [0], 'OTL': [0], 'OTU': [0],
    'MOV': [1],
    'ADD': [2], 'SUB': [2], 'MUL': [2], 'DIV': [2],
    'TRN': [1],
    'TON': [0], 'RTO': [0], 'CTU': [0], 'CTD': [0], 'RES': [0],
}
def is_tag_operand(operand) -> bool:
    operand = operand.strip()
    if not operand or operand =='?' or ' ' in operand or operand in NOT_A_TAG:
        return False
    if operand[0].isdigit() or operand[0] in '-+.':
        return False
    return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_:.\[\]]*$',operand))

def base_tag(operand):
    return re.split(r'[.\[]',operand, 1)[0]

def station_of(program_name):
    match = re.match(r'_(\d+)_', program_name)
    return match.group(1) if match else None

def read_delclarations(root):
    
    found_tags = {}   
    for tags in root.iter('Tags'):
        for tag in tags:
            name = tag.get('Name')
            desc = tag.find('Description').text if tag.find('Description') else None
            found_tags[base_tag(name)] =  {
                'data_type' : tag.get('DataType'),
                'radix' : tag.get('Radix'),
                'tag_type' : tag.get('TagType'),
                'alias_for' : tag.get('AliasFor'),
                'description' :desc
            }
    return found_tags
    


def read_references(root):
    references = []
    for program in root.iter('Program'):
        if program.get('Use') != 'Target':
            continue
        program_name = program.get('Name')
        station = station_of(program_name)

        for routine in program.iter('Routine'):
            routine_name = routine.get('Name')

            for rung in root.iter('Rung'):
                text_element = rung.find('Text').text
                if text_element is None:
                    continue
                rung_text = text_element

                for instruction,operands in tag_calls(rung_text):
                    if instruction == 'JSR':
                        continue
                    for position, operand in enumerate(operands):
                        if not is_tag_operand(operand):
                            continue
                        references.append({
                            'tag' : base_tag(operand),
                            'program' : program_name,
                            'station' : station,
                            'routine' : routine_name,
                            'rung': rung_text,
                            'instruction' : instruction,
                            'position' : position,
                            'is_write' : position in  WRITES.get(instruction, [])
                        })
    return references

def load_all(file_paths):
    master_references = []
    master_declarations = {}
    for file in file_paths:
        print(f'File currently in {file}')
        tree = ET.parse(f'{current_dir}/{file}')
        root = tree.getroot()
        master_references.extend(read_references(root))
        declarations = read_delclarations(root) 
        master_declarations.update(declarations)
    return master_declarations,master_references
        

def find_owners(references):
    writers = {}
    for ref in references:
        if ref['is_write']:
            writers.setdefault(ref['tag'], set()).add(ref['station'])

    owners = {}
    ambiguous = {}
    for tag, stations in writers.items():
        if len(stations) == 1:
            owners[tag] = next(iter(stations))
        else:
            ambiguous[tag] = stations
    return owners, ambiguous

def find_limits(references):
    tag_limits={}
    for ref in references:
        if ref['instruction'] == 'LIM':
            is_circular = False
            rung = ref['rung']
            for instruction,operands in tag_calls(rung):
                if instruction == 'LIM':
                    oper = operands

            low,value,high = oper
            value = base_tag(value)
            if not is_tag_operand(low) and not is_tag_operand(high):
                if low > high:
                    is_circular = True 
            tag_limits[value] = {
                'low' : low,
                'high' : high,
                'circular' : is_circular
            }
    return tag_limits

def is_hmi_plumbing(desc):
    HMI_indicators = ['HMI PUSH BUTTON','HMI VISIBILITY','HMI ANIMATION','HMI INDICATOR']
    if desc is None:
        return False
    for indicator in HMI_indicators:
        if indicator in desc:
            return True
    return False

def extract_unit(desc):
    UNITS = []
    if not isinstance(desc, str):
        return None
    return re.findall(r'(\w+)', desc)

class Parameter:
    def __init__(this,name,station,datatype,radix,alias_for,unit,min_value,max_value,circular,description):
        this.name = name
        this.station = station
        this.datatype = datatype
        this.radix = radix,
        this.alias_for = alias_for
        this.unit = unit
        this.min_value = min_value
        this.max_value = max_value,
        this.circular = circular,
        this.description = description

  
    def __str__(self):
        return "This object contains:\n Tag: %s \n " \
        "Station : %s \n" \
        "Unit of Measurement: %s \n" \
        "DataType: %s \n" \
        "Radix : %s \n" \
        "Alias For: %s \n" \
        "Min Value: %s \n" \
        "Max Value %s \n" \
        "Circular : %s \n" \
        "Descripition: %s \n" % (self.name,self.station,self.unit,self.datatype,self.radix,self.alias_for,self.min_value,self.max_value,self.circular,self.description)

    def __repr__(self):
        return str(self)


def build_parameters(declarations,owners,limits):
    parameter_list = []
    for owner in owners.items():
        tag = owner[0]
        if tag in declarations:
            declaration = declarations[tag]
        else:
            continue

        description = declaration['description']# if type(declaration['description']) is str else None
        if not is_hmi_plumbing(description):
            if tag in limits:
                low = limits[tag]['low']
                high = limits[tag]['high']
                circular = limits[tag]['circular']
            else:
                low = high = circular = None
           

            tag_object = Parameter(
                tag,
                owner[1],
                declaration['data_type'],
                declaration['radix'],
                declaration['alias_for'],
                extract_unit(description),
                low,
                high,
                circular,
                description
            )
            parameter_list.append(tag_object)
    return parameter_list



def generate_explorer_graph(declarations, references, max_nodes=2000):
    """
    Overhauled explorer graph builder that pre-calculates node coordinates 
    in Python to prevent the browser from freezing.
    """
    import networkx as nx
    from pyvis.network import Network

    G = nx.DiGraph()
    seen_edges = set()
    
    # 1. Build the NetworkX graph in Python memory
    for ref in references:
        if G.number_of_nodes() >= max_nodes:
            print(f"⚠️ Graph capped at {max_nodes} nodes to ensure instant loading.")
            break
            
        station_id = f"Station_{ref['station']}" if ref['station'] else "Global_Station"
        prog_id = f"Prog_{ref['program']}"
        rout_id = f"Routine_{ref['program']}_{ref['routine']}"
        tag_id = f"Tag_{ref['tag']}"
        
        # Add metadata fields for visual identification
        G.add_node(station_id, label=ref['station'] or "Global", group="Station", color="#FF5733")
        G.add_node(prog_id, label=ref['program'], group="Program", color="#33FFCE")
        G.add_node(rout_id, label=ref['routine'], group="Routine", color="#3380FF")
        
        G.add_edge(station_id, prog_id, relationship="HAS_PROGRAM")
        G.add_edge(prog_id, rout_id, relationship="HAS_ROUTINE")
        
        tag_meta = declarations.get(ref['tag'], {})
        desc_text = tag_meta.get('description', '') or 'No Description'
        
        G.add_node(tag_id, 
                   label=ref['tag'], 
                   group="Tag", 
                   color="#9B59B6",
                   title=f"Type: {tag_meta.get('data_type')}\nDesc: {desc_text}")
        
        edge_key = (rout_id, tag_id) if ref['is_write'] else (tag_id, rout_id)
        if edge_key not in seen_edges:
            seen_edges.add(edge_key)
            if ref['is_write']:
                G.add_edge(rout_id, tag_id, relationship="WRITES_TO", color="#E74C3C")
            else:
                G.add_edge(tag_id, rout_id, relationship="READS", color="#2ECC71")

    # 2. PRE-CALCULATE COORDINATES IN PYTHON
    # This prevents the web browser from running heavy math loops
    print("Calculating node layout positions...")
    pos = nx.spring_layout(G, k=0.5, iterations=50)

    # 3. Initialize PyVis network map
    net = Network(notebook=False, height="900px", width="100%", directed=True, heading="L5X Manufacturing Tag Explorer")
    
    # 4. Inject nodes manually with fixed X and Y coordinates
    for node_id, data in G.nodes(data=True):
        x, y = pos[node_id]
        # Multiply position variables to scale out the map cleanly
        net.add_node(node_id, 
                     label=data['label'], 
                     group=data['group'], 
                     color=data['color'],
                     title=data.get('title', ''),
                     x=int(x * 3000), 
                     y=int(y * 3000),
                     physics=False) # STRICT FIX: Disable physics on individual nodes

    # Inject edges manually
    for source, target, data in G.edges(data=True):
        net.add_edge(source, target, color=data.get('color', '#848484'))

    # 5. ABSOLUTE ZERO PHYSICS SETTINGS FOR THE BROWSER
    net.set_options("""
    var options = {
      "physics": {
        "enabled": false
      },
      "interaction": {
        "hover": true,
        "navigationButtons": true,
        "hideEdgesOnDrag": true,
        "hideEdgesOnZoom": true
      }
    }
    """)
    
    output_filename = "manufacturing_tag_graph.html"
    net.save_graph(output_filename)
    print(f"🚀 Success! Fixed graph generated at: {output_filename}")





declarations,references = load_all(files)
owners, ambigious = find_owners(references)
print(f'Tags with no obvious owner: {ambigious}')
limits = find_limits(references)
parameters = build_parameters(declarations,owners,limits)
generate_explorer_graph(declarations,references)
for limit in limits:
    print(limit)
for parameter in list(parameters):
    print(parameter)
    input()

    