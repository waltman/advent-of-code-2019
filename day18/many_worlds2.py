#!/usr/bin/env python3
from sys import argv
from Grid import Grid
from copy import deepcopy
from collections import deque

cache = {}

def min_dist(grid, k, d, ch):
    global cache

    g2 = deepcopy(grid)
    r,c = g2.pos_of[k]
    g2.remove(k)
    g2.remove(k.upper())
    g2.change_current_pos(r,c,ch)
    vis = g2.all_visible_keys()
    vis_keys = ','.join(sorted([k for d,k,ch in vis]))
    p1 = g2.pos_of['1']
    p2 = g2.pos_of['2']
    p3 = g2.pos_of['3']
    p4 = g2.pos_of['4']
    if (k, vis_keys, p1, p2, p3, p4) in cache:
        return d + cache[(k, vis_keys, p1, p2, p3, p4)]

    if len(vis) == 0:
        result = 0
    else:
        result = min([min_dist(g2, k2, d2, ch2) for d2,k2,ch2 in vis])
        
    cache[(k, vis_keys, p1, p2, p3, p4)] = result
    return d + result
    
filename = argv[1]
grid = Grid()
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        grid.add_row(line)

print(grid)

visible = grid.all_visible_keys()
print(visible)
print('Part 2:', min([min_dist(grid, k, d, ch) for d,k,ch in visible]))
