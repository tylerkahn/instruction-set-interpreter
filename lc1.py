import sys
from array import array

register = array('i', [0, 0, 0, 0, 0, 0, 0, 0])

def deref_argument(s):
    if s.isdigit():
        return 0xFFFF & int(s)
    elif s[:2] == "0x":
        return 0xFFFF & int(s, 16)
    elif s[0] == 'r':
        return 0xFFFF & register[int(s[1])]
    else:
        print s, "not handled"
        sys.exit(-1)
        

def deref_all_but_last(func):
    def wrapper(*args, **kwargs):
        last_arg = int(args[-1][1])
        args = map(deref_argument, args[0:-1]) + [last_arg]
        return func(*args, **kwargs)
    return wrapper

def deref_all(func):
    def wrapper(*args, **kwargs):
        return func(*map(deref_argument, args), **kwargs)
    return wrapper

@deref_all_but_last
def add(v1, v2, n):
    register[n] = v1 + v2

@deref_all_but_last
def not_(v1, n):
    register[n] = ~v1

@deref_all_but_last
def and_(v1, v2, n):
    register[n] = v1 & v2

@deref_all_but_last
def mov(v1, n):
    register[n] = v1

@deref_all
def dsp(v1):
    sys.stdout.write(chr(v1))


''' Special Instructions'''
    
@deref_all
def print_(v1):
    print "0x" + hex(v1)[2:].upper()

''' Interpreter '''


def handle_instruction(s):
    if s in ["not", "or", "and", "print"]: # these are python keywords
        return s + "_"
    else:
        return s
    
with open(sys.argv[1], 'r') as f:
    code = f.readlines()
    code = map(lambda x: x.split(';')[0].strip().lower(), code) # remove comments and extraneous whitespace
    code = filter(lambda x: x != '', code) #remove blank lines

while code:
    line = code.pop(0).split() # [Instruction, arg1, arg2, ...]
    
    instruction = handle_instruction(line.pop(0))
    arguments = line
    apply(eval(instruction), arguments)
