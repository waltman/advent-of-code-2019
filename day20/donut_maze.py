#!/usr/bin/env python3
from sys import argv
from collections import defaultdict, deque

def draw_grid(grid, rows, cols):
    s = ''
    s += '      '
    for c in range(cols):
        s += str(c // 10)
    s += "\n"
    s += '      '
    for c in range(cols):
        s += str(c % 10)
    s += "\n"
    
    for r in range(rows):
        s += f'{r:5d} '
        for c in range(cols):
            s += grid[r][c]
        s += "\n"
    print(s)

grid = []
rows = 0
cols = 0

filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip("\n")
        if cols == 0:
            cols = len(line)
        grid.append(list(line))
        rows += 1

draw_grid(grid, rows, cols)

portals = defaultdict(list)
start = ()
finish = ()
# top row
for c in range(cols):
    if grid[0][c].isupper():
        k = grid[0][c] + grid[1][c]
        pos = (2,c)
        if k == 'AA':
            start = pos
        elif k == 'ZZ':
            finish = pos
        else:
            portals[k].append(pos)

# bottom row
for c in range(cols):
    if grid[rows-2][c].isupper():
        k = grid[rows-2][c] + grid[rows-1][c]
        pos = (rows-3,c)
        if k == 'AA':
            start = pos
        elif k == 'ZZ':
            finish = pos
        else:
            portals[k].append(pos)

# middle
for row in range(2,rows-2):
    # left
    if grid[row][0].isupper():
        k = grid[row][0] + grid[row][1]
        pos = (row, 2)
        if k == 'AA':
            start = pos
        elif k == 'ZZ':
            finish = pos
        else:
            portals[k].append(pos)

    # right
    if grid[row][cols-2].isupper():
        k = grid[row][cols-2] + grid[row][cols-1]
        pos = (row, cols-3)
        if k == 'AA':
            start = pos
        elif k == 'ZZ':
            finish = pos
        else:
            portals[k].append(pos)

    # middle
    for col in range(2, cols-2):
        if grid[row][col].isupper():
            if grid[row][col+1].isupper(): # across
                k = grid[row][col] + grid[row][col+1]
                if grid[row][col+2] == ' ': # left
                    pos = (row,col-1)
                else: # right
                    pos = (row,col+2)
                portals[k].append(pos)
                    
            elif grid[row+1][col].isupper(): # down
                k = grid[row][col] + grid[row+1][col]
                if grid[row+2][col] == ' ': # top
                    pos = (row-1,col)
                else: # bottom
                    pos = (row+2,col)
                portals[k].append(pos)

print(f'{start=} {finish=} {portals=}')
warp = {}
for p1,p2 in portals.values():
    warp[p1] = p2
    warp[p2] = p1
print(f'{warp=}')

# now run BFS to find the shortest path from start to finish
queue = deque()
queue.append((start, 0))
seen = set()
while queue:
    pos, dist = queue.popleft()
    if pos == finish:
        print('Part 1:', dist)
        break

    seen.add(pos)
    if pos in warp:
        if warp[pos] not in seen:
            queue.append((warp[pos], dist+1))

    row, col = pos
    if grid[row-1][col] == '.' and (row-1,col) not in seen:
        queue.append(((row-1,col), dist+1))
    if grid[row+1][col] == '.' and (row+1,col) not in seen:
        queue.append(((row+1,col), dist+1))
    if grid[row][col-1] == '.' and (row,col-1) not in seen:
        queue.append(((row,col-1), dist+1))
    if grid[row][col+1] == '.' and (row,col+1) not in seen:
        queue.append(((row,col+1), dist+1))
