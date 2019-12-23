#!/usr/bin/env python3
from sys import argv
from Grid import Grid

filename = argv[1]
grid = Grid()
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        grid.add_row(line)

print(f'{grid.rows}, {grid.cols}')
print(grid)
print(grid.grid[1][3])
print(grid.get(1,3))

print(grid.current_pos())
print(grid.visible_keys())
