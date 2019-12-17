#!/usr/bin/env python3
from sys import argv

def pattern_val(i, n):
    '''return the ith value of the pattern when repeated n times'''
    if i < n:
        return 0
    elif i < n*2:
        return 1
    elif i < n*3:
        return 0
    else:
        return -1

def process_signal(signal, num_phases):
    sig = signal
    for phase in range(1,num_phases+1):
        new_sig = ''
        for i in range(1, len(signal)+1):
            pattern_len = i * 4
            j = 1
            val = 0
            for d in sig:
                val += int(d) * pattern_val(j % pattern_len, i)
                j += 1
            new_sig += str(abs(val) % 10)
        sig = new_sig
    return sig


# read in the program
filename = argv[1]
with open(filename) as f:
    signal = f.readline().rstrip()

orig_sig = signal
PHASES=100
print('Part1:', process_signal(signal, PHASES)[:8])

signal = orig_sig * 10_000
offset = int(signal[0:7])

subsig = [int(s) for s in signal[offset:]]
for p in range(PHASES):
    new_sig = [subsig[-1]]
    for i in range(len(subsig)-2,-1,-1):
        new_sig.append(subsig[i] + new_sig[-1])
    subsig = [x % 10 for x in new_sig[::-1]]
s = ''.join([str(x) for x in subsig[:8]])
print('Part2:', s)



        
