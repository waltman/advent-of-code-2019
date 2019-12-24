#!/usr/bin/env python3
from sys import argv
from Grid import Grid
from copy import deepcopy
from collections import deque

cache = {}

def min_dist(grid, k, d):
    global cache

#    print(f'{k=} {d=}')
    g2 = deepcopy(grid)
    r,c = g2.pos_of[k]
    g2.remove(k)
    g2.remove(k.upper())
    g2.change_current_pos(r,c)
    vis = g2.visible_keys()
    vis_keys = ','.join(sorted([k for d,k in vis]))
#    print(f'{vis=} {vis_keys=} {cache=}')
    if (k, vis_keys) in cache:
        return d + cache[(k, vis_keys)]

    if len(vis) == 0:
        result = 0
    else:
        result = min([min_dist(g2, k2, d2) for d2,k2 in vis])
        
    cache[(k, vis_keys)] = result
    return d + result
    

# def min_path(grid, k, d):
#     global cache
#     g2 = deepcopy(grid)
#     r,c = g2.pos_of[k]
#     g2.remove(k)
#     g2.remove(k.upper())
#     g2.change_current_pos(r,c)
#     vis = g2.visible_keys()
#     if len(vis) == 0:
#         return d
#     else:
#         return d + min([min_path(g2, k2, d2) for k2,d2 in vis])

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
print(sorted(grid.visible_keys(),reverse=True))

visible = grid.visible_keys()
print('Part 1:', min([min_dist(grid, k, d) for d,k in visible]))
      
# best_len = 1e100
# stack = []
# for d,k in sorted(grid.visible_keys(),reverse=True):
#     stack.append((grid,[],k,d))
# while stack:
# #    print(f'{best_len=}, {len(stack)=}')
#     g, path, k, d = stack.pop()
#     g2 = deepcopy(g)
#     p2 = path.copy()
#     p2.append(k)
#     r,c = g2.pos_of[k]
#     g2.remove(k)
#     g2.remove(k.upper())
#     g2.change_current_pos(r,c)
#     vis = sorted(g2.visible_keys(),reverse=True)
#     if len(vis) == 0:
#         best_len = min(best_len, d)
#         print(f'{best_len=}, {p2=}, {len(stack)=}')
#     else:
#         for d2,k2 in vis:
#             if d + d2 < best_len:
#                 stack.append((g2, p2, k2, d+d2))
    
# print('Part 1:', best_len)


