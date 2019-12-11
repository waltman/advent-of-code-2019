#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

def turn_left(c):
    if c == complex(1,0):
        return complex(0,1)
    elif c == complex(0,1):
        return complex(-1,0)
    elif c == complex(-1,0):
        return complex(0,-1)
    else:
        return complex(1,0)

def turn_right(c):
    if c == complex(1,0):
        return complex(0,-1)
    elif c == complex(0,-1):
        return complex(-1,0)
    elif c == complex(-1,0):
        return complex(0,1)
    else:
        return complex(1,0)

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

grid = defaultdict(int)
pos = complex(0,0)
dir = complex(0,1) # up
vc = Intcode(pgm, 0)
while True:
    color = vc.run()
    if vc.halted:
        break
    grid[pos] = color

    turn = vc.run()
    if turn == 0:
        dir = turn_left(dir)
    else:
        dir = turn_right(dir)
    pos += dir
    vc.input = grid[pos]

print('Part 1:', len(grid))
