from l5x import l5x
from tokenizer import tokenizer
from os import listdir
from os.path import isfile, join

current_dir = 'Chris_AC13'
files = [f for f in listdir(current_dir) if isfile(join(current_dir, f))]

declarations,references = l5x.load_all(files,current_dir)

for ref in references[:15]:
    print(ref)
