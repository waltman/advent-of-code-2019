#!/usr/bin/env python3
from sys import argv
from itertools import permutations
from Intcode import Intcode

# run the amps in the order listed and return the output signal
def run_amps(pgm, order):
    output_sig = 0
    for phase in order:
        vc = Intcode(pgm, phase, output_sig)
        output_sig = vc.run()
    return output_sig

# run the amps in a feedback loop
def run_feedback_amps(pgm, order):
    vcs = [Intcode(pgm, phase) for phase in order]
    output_sig = 0
    i = 0
    while True:
        if vcs[i].halted:
            print(f'vcs {i} unexpectedly halted!')
            return 0
        
        vcs[i].input = output_sig
        output_sig = vcs[i].run()
        if i == len(vcs)-1 and vcs[i].halted:
            return output_sig

        i = (i + 1) % len(vcs)

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

amps = [x for x in range(5)]
perms = permutations(amps)
print('Part 1:', max([run_amps(pgm, order) for order in perms]))

amps = [x for x in range(5, 10)]
perms = permutations(amps)
print('Part 2:', max([run_feedback_amps(pgm, order) for order in perms]))
