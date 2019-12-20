#!/usr/bin/env python3
from sys import argv
from collections import defaultdict, deque
from Intcode import Intcode

ROWS = 41+2
COLS = 45+2

def draw_grid(grid):
    s = ''
    for r in range(ROWS):
        for c in range(COLS):
            s += grid[r][c]
        s += "\n"
    print(s)

def is_intersection(grid,r,c):
    return (grid[r][c]   == '#' and
            grid[r][c-1] == '#' and
            grid[r][c+1] == '#' and
            grid[r-1][c] == '#' and
            grid[r+1][c] == '#')

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

# read in the grid
vc = Intcode(pgm,0)
grid = [['.' for x in range(COLS)] for y in range(ROWS)]
row = 0
col = 0
while True:
    i = vc.run()
    if vc.halted:
        break
    ch = chr(int(i))
    if ch == '\n':
        row += 1
        col = 0
    else:
        grid[row+1][col+1] = ch
        col += 1

draw_grid(grid)

# count sum of intersection points
tot = 0
for r in range(1, ROWS-1):
    for c in range(1,COLS-1):
        if is_intersection(grid, r, c):
            tot += (r-1) * (c-1)
print('Part 1:', tot)
