#!/usr/bin/env python3
from sys import argv
from collections import defaultdict, deque
from Intcode import Intcode
import re

ROWS = 41+2
COLS = 45+2

def draw_grid(grid):
    s = ''
    for r in range(ROWS):
        for c in range(COLS):
            s += grid[r][c]
        s += "\n"
    print(s)

def is_intersection(grid,r,c):
    return (grid[r][c]   == '#' and
            grid[r][c-1] == '#' and
            grid[r][c+1] == '#' and
            grid[r-1][c] == '#' and
            grid[r+1][c] == '#')

def turn(grid, pos, dir):
    right = {complex(0,1): complex(-1,0),
             complex(1,0): complex(0,1),
             complex(0,-1): complex(1,0),
             complex(-1,0): complex(0,-1)
    }
    left = {complex(0,1): complex(1,0),
            complex(1,0): complex(0,-1),
            complex(0,-1): complex(-1,0),
            complex(-1,0): complex(0,1)
    }

    l = pos + left[dir]
    r = pos + right[dir]
    if grid[int(l.imag)][int(l.real)] == '#':
        return 'L', left[dir]
    elif grid[int(r.imag)][int(r.real)] == '#':
        return 'R', right[dir]
    else:
        return '', complex(0,0)

def make_routine(s, patterns):
    name = ['A','B','C']
    routine = []
    start = 0
    while start < len(s):
        found = False
        for i in range(len(patterns)):
            if re.search(f'^{patterns[i]}', s[start:]):
                routine.append(name[i])
                start += len(patterns[i])+1
                found = True
                break
        if not found:
            return
    return routine

def make_program(s):
    start_i = 0
    for i in range(start_i+20,start_i+5,-1):
        if not s[i].isdigit():
            continue
        A = s[start_i:i+1]
        start_j = i+2
        while s[start_j:start_j+len(A)] == A:
            start_j += len(A)+1
        for j in range(start_j+20,start_j+5,-1):
            if j >= len(s):
                continue
            if not s[j].isdigit():
                continue
            B = s[start_j:j+1]
            start_k = j+2
            while True:
                if s[start_k:start_k+len(A)] == A:
                    start_k += len(A)+1
                    continue
                if s[start_k:start_k+len(B)] == B:
                    start_k += len(B)+1
                    continue
                break
            for k in range(start_k+20,start_k+5,-1):
                if k >= len(s):
                    continue
                if not s[k].isdigit():
                    continue
                C = s[start_k:k+1]
                res = make_routine(s, [s[start_i:i+1],s[start_j:j+1],s[start_k:k+1]])
                if res:
                    return(','.join(res), A, B, C)
        

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

# read in the grid
vc = Intcode(pgm,0)
grid = [['.' for x in range(COLS)] for y in range(ROWS)]
row = 0
col = 0
while True:
    i = vc.run()
    if vc.halted:
        break
    ch = chr(int(i))
    if ch == '\n':
        row += 1
        col = 0
    else:
        grid[row+1][col+1] = ch
        col += 1

draw_grid(grid)

# count sum of intersection points
tot = 0
for r in range(1, ROWS-1):
    for c in range(1,COLS-1):
        if is_intersection(grid, r, c):
            tot += (r-1) * (c-1)
print('Part 1:', tot)

# find the start point
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '^':
            print(r,c)
            pos = complex(c,r)
            break

# generate path
dir = complex(-1,0)
cmds = ['L']
dist = 0
while True:
    new_pos = pos + dir
    r = int(new_pos.imag)
    c = int(new_pos.real)
    if grid[r][c] == '#':
        dist += 1
        pos = new_pos
    else:
        cmds.append(str(dist))
        cmd, new_dir = turn(grid, pos, dir)
        if cmd == '':
            break
        else:
            cmds.append(cmd)
            dir = new_dir
            dist = 0

print(','.join(cmds))

# generate the program
res, A, B, C = make_program(','.join(cmds))
print('res =', res)
print('A =', A)
print('B =', B)
print('C =', C)
instructs = [ord(c) for c in f'{res}\n{A}\n{B}\n{C}\nn\n']

# rerun the vc with the program and get the output
vc = Intcode(pgm, 0)
vc.pgm[0] = 2
vc.input = instructs
while True:
    result = vc.run()
    if vc.halted:
        break
print('Part 2:', vc.last)
