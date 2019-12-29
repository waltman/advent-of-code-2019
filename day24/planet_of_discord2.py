#!/usr/bin/env python3
from sys import argv
from copy import deepcopy

SIZE = 5
MINUTES = 200
DEPTH = MINUTES+3

def adjacent(row,col,level):
    up_north = (1,2,level+1)
    up_east  = (2,3,level+1)
    up_south = (3,2,level+1)
    up_west  = (2,1,level+1)

    down_north = [(4,c,level-1) for c in range(SIZE)]
    down_east  = [(r,0,level-1) for r in range(SIZE)]
    down_south = [(0,c,level-1) for c in range(SIZE)]
    down_west  = [(r,4,level-1) for r in range(SIZE)]

    adj = []
    # n
    if row == 0:
        adj.append(up_north)
    elif (row,col) == (3,2):
        adj += down_north
    else:
        adj.append((row-1,col,level))
    # e
    if col == 4:
        adj.append(up_east)
    elif (row,col) == (2,1):
        adj += down_east
    else:
        adj.append((row,col+1,level))
    # s
    if row == 4:
        adj.append(up_south)
    elif (row,col) == (1,2):
        adj += down_south
    else:
        adj.append((row+1,col,level))
    # w
    if col == 0:
        adj.append(up_west)
    elif (row,col) == (2,3):
        adj += down_west
    else:
        adj.append((row,col-1,level))

    return adj

def stringify_grid(grid):
    s = ''
    for row in range(SIZE):
        for col in range(SIZE):
            if row == 2 and col == 2:
                s += '?'
            else:
                s += grid[row][col]
        s += '\n'
    return s

def evolve(grids):
    new_grids = [empty_grid() for _ in range(DEPTH)]
    for level in range(1, DEPTH-1):
        for row in range(SIZE):
            for col in range(SIZE):
                if (row,col) == (2,2):
                    continue
                adj = adjacent(row, col, level)
                cnt = len([(r1,c1,l1) for (r1,c1,l1) in adj if grids[l1][r1][c1] == '#'])
                if grids[level][row][col] == '#' and cnt != 1:
                    new_grids[level][row][col] = '.'
                elif grids[level][row][col] == '.' and 1 <= cnt <= 2:
                    new_grids[level][row][col] = '#'
                else:
                    new_grids[level][row][col] = grids[level][row][col]
    return new_grids

def empty_grid():
    return [['.' for col in range(SIZE)] for row in range(SIZE)]

def print_grids(grids):
    for i in range(DEPTH):
        print(f'Depth {i - DEPTH//2}:')
        print(stringify_grid(grids[i]))

# read in the input and initialize the stack of grids
grids = [empty_grid() for _ in range(DEPTH)]
grid = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        grid.append(list(line))
grids[DEPTH//2] = grid

# evolve the bugs for MINUTES minutes
for minute in range(MINUTES):
    new_grids = evolve(grids)
    for level in range(1, DEPTH-1):
        for row in range(SIZE):
            for col in range(SIZE):
                if (row,col) == (2,2):
                    continue
                grids[level][row][col] = new_grids[level][row][col]

# count up the bugs
cnt = 0
for level in range(1, DEPTH-1):
    for row in range(SIZE):
        for col in range(SIZE):
            if (row,col) == (2,2):
                continue
            if grids[level][row][col] == '#':
                cnt += 1
print('Part 2:', cnt)
