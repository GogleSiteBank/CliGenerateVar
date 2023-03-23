import argparse
import random, string, sys

## arg parse stuff

parser = argparse.ArgumentParser(
                    prog='Generate Types',
                    description='General random variable types.')

parser.add_argument("--type", help = "String, integer, boolean, etc")

parser.add_argument("-len", help = "length")

types = ["int", "bool", "string", "float"]
joined = ", ".join(types)
parser.usage = f"[{parser.prog}] [{parser.description}]\nValid types = {joined}\n--type -len" 

args = parser.parse_args()
try:
    gettype = args.type.lower()
except AttributeError:
    print("Attribute Error, did you enter a type?")
    sys.exit()

######

def generatestring(len = 12):
    abc =  "".join(random.choices(string.ascii_letters, k=len))
    return abc

def generateint(len = 10):
    abc = random.randint(0, len)
    return abc

def generatebool(len = None):
    if Len is None:
        ab = [1,2]
        choice = random.choice(ab)
        if choice == 1:
            return True
        else: return False
    else: return "Len not valid for bool"

def generatefloat(len = 10):
    abc = random.uniform(0, len)
    return abc

if gettype in types:
    if not args.len:
        print(f"Valid type: {gettype}")
        for _ in types:
            if gettype == _:
                e = f"print(generate{_}())"
                exec(e)
    else:
        print(f"Valid type & len: {gettype} {args.len}")
        for _ in types:
            if gettype == _:
                e = f"print(generate{_}({args.len}))"
                exec(e)
else:
    print(f"Invalid type: {gettype}")
