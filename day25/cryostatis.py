#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

vc = Intcode(pgm, 0)
s = ''
while True:
    result = vc.run()
    s += chr(result)
    if s.endswith('Command?\n'):
        cmd = input(s)
        cmd += '\n'
        s = ''
        vc.input = [ord(c) for c in cmd]



