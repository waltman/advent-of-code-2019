#!/usr/bin/env python3
from sys import argv
from collections import defaultdict, deque
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

vc = Intcode(pgm,0)
s = ''

while True:
    i = vc.run()
    if vc.halted:
        break
    s += chr(int(i))

print(s)
