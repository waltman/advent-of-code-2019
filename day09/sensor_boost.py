#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

vc = Intcode(pgm, 1)
while True:
    output = vc.run()
    print(output)
    if vc.halted:
        print('Part 1:', output)
        break

vc = Intcode(pgm, 2)
while True:
    output = vc.run()
    print(output)
    if vc.halted:
        print('Part 2:', output)
        break
