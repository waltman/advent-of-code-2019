#!/usr/bin/env python3
from sys import argv
from Grid import Grid
from copy import deepcopy

def min_path(grid, k, d):
    g2 = deepcopy(grid)
    r,c = g2.pos_of[k]
    g2.remove(k)
    g2.remove(k.upper())
    g2.change_current_pos(r,c)
    vis = g2.visible_keys()
    if len(vis) == 0:
        return d
    else:
        return d + min([min_path(g2, k2, d2) for k2,d2 in vis])

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

print('Part 1:', min([min_path(grid, k, d) for k,d in grid.visible_keys()]))
