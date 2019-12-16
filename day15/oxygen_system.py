#!/usr/bin/env python3
from sys import argv
from collections import defaultdict, deque
from Intcode import Intcode

SIZE = 50

def draw_grid(grid):
    s = ''
    for r in range(SIZE):
        for c in range(SIZE):
            s += grid[r][c]
        s += "\n"
    print(s)

DIRS = {complex(0,-1): 1, #up
        complex(1,0):  4, #right
        complex(0,1):  2, #down
        complex(-1,0): 3, #left
}
DIR_QUEUE = [k for k in DIRS.keys()]

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

grid = [[' ' for x in range(SIZE+1)] for y in range(SIZE+1)]
    
vc = Intcode(pgm,1)
seen = set()
dqueue = DIR_QUEUE[::-1]
pos = complex(SIZE//2,SIZE//2)
grid[SIZE//2][SIZE//2] = 'X'
seen.add(pos)
path = []

while True:
    if len(dqueue) == 0:
        if len(path) == 0:
            print('done')
            break
        dir = path.pop()
        pos += dir
        vc.input = DIRS[dir]
        _ = vc.run()
        dqueue = DIR_QUEUE[::-1]
        continue
    else:
        dir = dqueue.pop()
        if pos + dir in seen:
            continue
    
    new_pos = pos + dir
    if new_pos.real < 0 or new_pos.real >= SIZE or new_pos.imag < 0 or new_pos.imag >= SIZE:
        continue
    seen.add(new_pos)

    vc.input = DIRS[dir]
    resp = vc.run()
    row = int(new_pos.imag)
    col = int(new_pos.real)
    if resp == 0:
        grid[row][col] = '#'
        continue
    elif resp == 1:
        grid[row][col] = '.'
    elif resp == 2:
        grid[row][col] = 'O'
        oxy_row = row
        oxy_col = col
    else:
        print('unexpected resp of', resp)
        break

    pos += dir
    path.append(-dir)
    dqueue = DIR_QUEUE[::-1]

draw_grid(grid)

queue = deque()
queue.append((SIZE//2,SIZE//2,0))
seen2 = set()
while True:
    if not queue:
        break
    row, col, dist = queue.popleft()
    if grid[row][col] == 'O':
        break
    
    if (row,col) in seen2:
        continue
    else:
        seen2.add((row,col))

    if grid[row+1][col] != '#':
        queue.append((row+1,col,dist+1))
    if grid[row-1][col] != '#':
        queue.append((row-1,col,dist+1))
    if grid[row][col+1] != '#':
        queue.append((row,col+1,dist+1))
    if grid[row][col-1] != '#':
        queue.append((row,col-1,dist+1))

print('Part1:', dist)

queue = deque()
queue.append((oxy_row,oxy_col,0))
seen2 = set()
max_dist = 0
while True:
    if not queue:
        break
    row, col, dist = queue.popleft()
    
    if (row,col) in seen2:
        continue
    else:
        seen2.add((row,col))
        grid[row][col] = 'O'
        max_dist = max(max_dist, dist)

    if grid[row+1][col] != '#':
        queue.append((row+1,col,dist+1))
    if grid[row-1][col] != '#':
        queue.append((row-1,col,dist+1))
    if grid[row][col+1] != '#':
        queue.append((row,col+1,dist+1))
    if grid[row][col-1] != '#':
        queue.append((row,col-1,dist+1))

print('Part2:', max_dist)
