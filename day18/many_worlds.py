#!/usr/bin/env python3
from sys import argv
from Grid import Grid
from copy import deepcopy
from collections import deque

cache = {}

def min_dist(grid, k, d):
    global cache

    g2 = deepcopy(grid)
    r,c = g2.pos_of[k]
    g2.remove(k)
    g2.remove(k.upper())
    g2.change_current_pos(r,c)
    vis = g2.visible_keys()
    vis_keys = ','.join(sorted([k for d,k in vis]))
    if (k, vis_keys) in cache:
        return d + cache[(k, vis_keys)]

    if len(vis) == 0:
        result = 0
    else:
        result = min([min_dist(g2, k2, d2) for d2,k2 in vis])
        
    cache[(k, vis_keys)] = result
    return d + result
    
filename = argv[1]
grid = Grid()
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        grid.add_row(line)

print(grid)

print(grid.visible_keys())

visible = grid.visible_keys()
print('Part 1:', min([min_dist(grid, k, d) for d,k in visible]))
