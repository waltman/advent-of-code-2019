#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

ROWS = 50
COLS = 50

def draw_grid(grid):
    s = ''
    for r in range(ROWS):
        for c in range(COLS):
            s += grid[r][c]
        s += "\n"
    print(s)

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

# read in the grid
vc = Intcode(pgm,0)
part1 = 0
grid = [['.' for x in range(COLS)] for y in range(ROWS)]
for row in range(ROWS):
    for col in range(COLS):
        vc = Intcode(pgm,0)
        vc.input = [col,row]
        vc.input_ptr = 0
        res = vc.run()
        if res == 0:
            grid[row][col] = '.'
        elif res == 1:
            grid[row][col] = '#'
            part1 += 1
        else:
            grid[row][col] = '?'

draw_grid(grid)
print('Part 1:', part1)
