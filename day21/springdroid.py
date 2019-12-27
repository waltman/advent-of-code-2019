#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

# copied from https://www.reddit.com/r/adventofcode/comments/edll5a/2019_day_21_solutions/
# also removed some unneeded commands
instruct_str = """NOT C T
OR A T
OR B J
NOT T J
AND C T
NOT T J
AND D J
WALK
"""
instructs = [ord(c) for c in instruct_str]

vc = Intcode(pgm, 0)
vc.input = instructs
s = ''
while True:
    result = vc.run()
    if result > 255:
        print('Part 1', result)
        break
    s += chr(result)
    if vc.halted:
        break
print(s)
