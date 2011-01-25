import sys
from array import array

register = array('i', [0, 0, 0, 0, 0, 0, 0, 0])

def add(v1, v2, n):
    register[n] = v1 + v2

def not_(v1, n):
    register[n] = ~v1

def and_(v1, v2, n):
    register[n] = v1 & v2

def mov(v1, n):
    register[n] = v1

def dsp(v1):
    sys.stdout.write(chr(v1))


''' Special Instructions'''
    
def print_(v1):
    print "0x" + hex(v1)[2:].upper()

''' Interpreter '''


def handle_argument(s):
    if s.isdigit():
        return 0xFFFF & int(s)
    elif s[:2] == "0x":
        return 0xFFFF & int(s, 16)
    elif s[0] == 'r':
        return 0xFFFF & register[int(s[1])]
    elif s[0] == '&':
        return int(s[2])
    else:
        print s, "not handled"
        sys.exit(-1)

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
    arguments = map(handle_argument, line)
    apply(eval(instruction), arguments)
    
    
    

