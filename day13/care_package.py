#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

num_blocks = 0
vc = Intcode(pgm, 0)
while True:
    x = vc.run()
    if vc.halted:
        break
    y = vc.run()
    if vc.halted:
        break
    tile = vc.run()
    if vc.halted:
        break
    print(x,y,tile)
    if tile == 2:
        num_blocks += 1
    
print('Part 1:', num_blocks)
