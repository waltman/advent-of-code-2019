#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

MAX_COL, MAX_ROW = 44, 23

def draw_grid(grid):
    tile = {0: ' ',
            1: '+',
            2: '#',
            3: '-',
            4: 'o'
        }

    s = ''
    for r in range(MAX_ROW+1):
        for c in range(MAX_COL+1):
            s += tile[grid[r][c]]
        s += "\n"
    print(s)

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

num_blocks = 0
grid = [[0 for x in range(MAX_COL+1)] for y in range(MAX_ROW+1)]
print(len(grid), len(grid[0]))
        
vc = Intcode(pgm, 0)
while True:
    c = vc.run()
    if vc.halted:
        break
    r = vc.run()
    if vc.halted:
        break
    tile = vc.run()
    if vc.halted:
        break
    print(r,c,tile)
    grid[r][c] = int(tile)
    if tile == 2:
        num_blocks += 1
    
print('Part 1:', num_blocks)
draw_grid(grid)

print('Part 2:')
vc = Intcode(pgm, 0)
vc.pgm[0] = 2
while True:
    c = vc.run()
    if vc.halted:
        break
    r = vc.run()
    if vc.halted:
        break
    tile = vc.run()
    if vc.halted:
        break
    print(r,c,tile)
    grid[r][c] = int(tile)
    if tile == 2:
        num_blocks += 1
