import re
import xml.etree.ElementTree as ET
from tokenizer import tokenizer
from models import Reference,Declaration


file = 'Chris_AC13/_04_BAR_PNC_Program.L5X'


class l5x:
    def read_references(root):
        references = []
        for program in root.iter('Program'):
            if program.get('Use') != 'Target':
                continue
            program_name = program.get('Name')
            station = tokenizer.station_of(program_name)

            for routine in program.iter('Routine'):
                routine_name = routine.get('Name')

                for rung in routine.iter('Rung'):
                    text_element = rung.find('Text').text
                    if rung.get('Number') is None:
                        continue
                    if text_element is None:
                        continue
                    rung_number = rung.get('Number')
                    rung_text = text_element

                    for instruction,operands in tokenizer.iter_calls(rung_text):
                        if instruction == 'JSR':
                            continue
                        for position, operand in enumerate(operands):
                            if not tokenizer.is_tag_operand(operand):
                                continue
                            ref = Reference(None,program_name,routine_name,rung_number,instruction,position,position in tokenizer.WRITES.get(instruction, []),None)
                            references.append(ref)
        return references


    def read_delclarations(root):
        
        found_tags = {}   
        parent_map = {c:p for p in root.iter( ) for c in p}

        for tags in root.iter('Tags'):
            for tag in tags:
                name = tag.get('Name')
                desc = tag.find('Description').text if tag.find('Description') else None
                declaration = Declaration(name,
                                        tag.get('DataType'),
                                        tag.get('Radix'),
                                        tag.get('TagType'),
                                        tag.get('AliasFor'),
                                        tag.get('Constant'),
                                        tag.get('ExternalAccess'),
                                        desc,
                                        parent_map[tags].tag)
                found_tags[parent_map[tags].tag,tokenizer.base_tag(name)] =  {declaration}
        return found_tags
        


    def load_all(file_paths,current_dir):
        master_references = []
        master_declarations = {}
        for file in file_paths:
            print(f'File currently in {file}')
            tree = ET.parse(f'{current_dir}/{file}')
            root = tree.getroot()
            master_references.extend(l5x.read_references(root))
            declarations = l5x.read_delclarations(root) 
            master_declarations.update(declarations)
        return master_declarations,master_references