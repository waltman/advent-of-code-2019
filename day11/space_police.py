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

grid = defaultdict(int)
pos = complex(0,5)
dir = complex(0,1) # up
vc = Intcode(pgm, 1)
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

print('Part 2:')
# I used this to find ROWS and COLS and pick the starting point on the grid
# to make drawing easier:
#
# print(grid.keys())
# min_i = 1e100
# min_j = 1e100
# max_i = -1e100
# max_j = -1e100
# for c in grid.keys():
#     min_i = min(min_i, c.real)
#     max_i = max(max_i, c.real)
#     min_j = min(min_j, c.imag)
#     max_j = max(max_j, c.imag)
    
# print(min_i, min_j, max_i, max_j)

s = ''
ROWS = 5
COLS = 42
for r in range(ROWS, -1, -1):
    for c in range(0, COLS+1):
        s += '*' if grid[complex(c,r)] == 1 else ' '
    s += '\n'
print(s)
