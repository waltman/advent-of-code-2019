#!/usr/bin/env python3
from sys import argv

def gen_pattern(n):
    pattern = []
    base = [0,1,0,-1]
    for x in base:
        pattern += [x] * n
    return pattern

def pattern_val(i, n):
    '''return the ith value of the pattern when repeated n times'''
    thresh = [j * n for j in range(1,4)]
#    print(f'{thresh=}')
    if i < thresh[0]:
        return 0
    elif i < thresh[1]:
        return 1
    elif i < thresh[2]:
        return 0
    else:
        return -1

# read in the program
filename = argv[1]
with open(filename) as f:
    signal = f.readline().rstrip()

PHASES=100
for phase in range(1,PHASES+1):
    new_sig = ''
    for i in range(1,len(signal)+1):
#        pattern = gen_pattern(i)
        pattern_len = i * 4
        j = 1
        val = 0
        for d in signal:
            val += int(d) * pattern_val(j % pattern_len, i)
            j += 1
#            print(int(d), pattern_val(j % pattern_len, phase), int(d) * pattern_val(j % pattern_len, phase), val)
        new_sig += str(abs(val) % 10)
#        print('new_sig=', new_sig)
#    print(phase, new_sig)
    signal = new_sig

print('Part1:', signal[:8])
