#!/usr/bin/env python3
from sys import argv

def gen_pattern(n):
    pattern = []
    base = [0,1,0,-1]
    for x in base:
        pattern += [x] * n
    return pattern

# read in the program
filename = argv[1]
with open(filename) as f:
    signal = f.readline().rstrip()

PHASES=100
for phase in range(1,PHASES+1):
    new_sig = ''
    for i in range(1,len(signal)+1):
        pattern = gen_pattern(i)
        j = 1
        val = 0
        for d in signal:
            val += int(d) * pattern[j % len(pattern)]
            j += 1
        new_sig += str(abs(val) % 10)
#    print(phase, new_sig)
    signal = new_sig

print('Part1:', signal[:8])
