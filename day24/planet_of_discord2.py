#!/usr/bin/env python3
from sys import argv
from copy import deepcopy

SIZE = 5
DEPTH = 13

def adjacent(row,col):
    adj = []
    # n
    if row > 0:
        adj.append((row-1,col))
    # s
    if row < SIZE-1:
        adj.append((row+1,col))
    # e
    if col < SIZE-1:
        adj.append((row,col+1))
    # w
    if col > 0:
        adj.append((row,col-1))

    return adj

def stringify_grid(grid):
    s = ''
    for row in range(SIZE):
        for col in range(SIZE):
            s += grid[row][col]
        s += '\n'
    return s

def evolve(grid):
    new_grid = [[' ' for col in range(SIZE)] for row in range(SIZE)]
    for row in range(SIZE):
        for col in range(SIZE):
            adj = adjacent(row, col)
            cnt = len([(r1,c1) for r1, c1 in adj if grid[r1][c1] == '#'])
            if grid[row][col] == '#' and cnt != 1:
                new_grid[row][col] = '.'
            elif grid[row][col] == '.' and 1 <= cnt <= 2:
                new_grid[row][col] = '#'
            else:
                new_grid[row][col] = grid[row][col]
    return new_grid

def biodiversity_rating(grid):
    tot = 0
    rating = 1
    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] == '#':
                tot += rating
            rating *= 2
    return tot

def empty_grid():
    return [['.' for col in range(SIZE)] for row in range(SIZE)]

def print_grids(grids):
    for i in range(DEPTH):
        print(f'Depth {i - DEPTH//2}:')
        print(stringify_grid(grids[i]))

grids = [empty_grid() for _ in range(DEPTH)]
grid = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        grid.append(list(line))
grids[DEPTH//2] = grid
print_grids(grids)

# seen = set()
# seen.add(stringify_grid(grid))
# while True:
#     new_grid = evolve(grid)
#     key = stringify_grid(new_grid)
#     if key in seen:
#         break
#     else:
#         seen.add(key)
#         grid = new_grid
# print(key)
# print('Part 1', biodiversity_rating(new_grid))
