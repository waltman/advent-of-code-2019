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

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

amps = [x for x in range(5)]
perms = permutations(amps)
print('Part 1:', max([run_amps(pgm, order) for order in perms]))
