
import re 
from models import Parameter


class tokenizer:


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

    def iter_calls(text):
        tokens = list(re.finditer(tokenizer.tok_regex, text))
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
                            operands.append(text[operand_start:tokens[j].start()].strip())
                    elif k == 'COMMA' and depth == 1:
                        operands.append(text[operand_start:tokens[j].start()].strip())
                        operand_start = tokens[j].end()
                    j += 1
                yield name, [o for o in operands if o]
                i = j
            else:
                i += 1


    def is_tag_operand(operand) -> bool:
        operand = operand.strip()
        if not operand or operand =='?' or ' ' in operand or operand in tokenizer.NOT_A_TAG:
            return False
        if operand[0].isdigit() or operand[0] in '-+.':
            return False
        return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_:.\[\]]*$',operand))

    def base_tag(operand):
        return re.split(r'[.\[]',operand, 1)[0]

    def station_of(program_name):
        match = re.match(r'_(\d+)_', program_name)
        return match.group(1) if match else None


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
                for instruction,operands in tokenizer.iter_calls(rung):
                    if instruction == 'LIM':
                        oper = operands

                low,value,high = oper
                value = tokenizer.base_tag(value)
                if not tokenizer.is_tag_operand(low) and not tokenizer.is_tag_operand(high):
                    if low > high:
                        is_circular = True 
                tag_limits[value] = {
                    'low' : low,
                    'high' : high,
                    'circular' : is_circular
                }
        return tag_limits


    def extract_unit(desc):
        UNITS = []
        if not isinstance(desc, str):
            return None
        return re.findall(r'(\w+)', desc)



    def build_parameters(declarations,owners,limits):
        parameter_list = []
        for owner in owners.items():
            tag = owner[0]
            if tag in declarations:
                declaration = declarations[tag]
            else:
                continue

            description = declaration['description']# if type(declaration['description']) is str else None
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
                    tokenizer.extract_unit(description),
                    low,
                    high,
                    circular,
                    description
                )
                parameter_list.append(tag_object)
        return parameter_list



    
                    
            
   
        