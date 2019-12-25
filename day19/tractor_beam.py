#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

ROWS = 50
COLS = 50

def draw_grid(grid):
    s = ''
    s += '      '
    for c in range(COLS):
        s += str(c // 10)
    s += "\n"
    s += '      '
    for c in range(COLS):
        s += str(c % 10)
    s += "\n"
    
    for r in range(ROWS):
        s += f'{r:5d} '
        for c in range(COLS):
            s += grid[r][c]
        s += "\n"
    print(s)

def is_beam(pgm, row, col):
    vc = Intcode(pgm,0)
    vc.input = [col,row]
    vc.input_ptr = 0
    res = vc.run()
    return res == 1

def left_edge(pgm, row):
    col = int(row * 0.78)
    while True:
        if is_beam(pgm, row, col):
            return col
        else:
            col += 1

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

SIZE = 99
row = 100
while True:
    col = left_edge(pgm, row)
    if is_beam(pgm, row-SIZE, col) and is_beam(pgm, row-SIZE, col+SIZE) and is_beam(pgm, row, col+SIZE):
       print(f'{row-SIZE=} {col=}')
       print('Part 2:', col * 10000 + row-SIZE)
       break
    row = row + 1

    
