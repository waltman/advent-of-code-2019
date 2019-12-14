#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

# constants from an initial debugging run
MAX_COL, MAX_ROW = 44, 23
PROW = 22

def draw_grid(grid):
    tile = {0: ' ',
            1: '+',
            2: '#',
            3: '-',
            4: 'o'
        }

    s = ''
    for r in range(MAX_ROW+1):
        for c in range(MAX_COL+1):
            s += tile[grid[r][c]]
        s += "\n"
    print(s)

def predict_hit_col(bpos, last_bpos):
    """Predict column where the ball impacts the paddle"""
    if last_bpos is None:
        return 22 # initial position

    drow = bpos[0] - last_bpos[0]
    dcol = bpos[1] - last_bpos[1]

    if drow < 0: # going up, just follow
        return bpos[1]
    elif dcol < 0: # going left
        return bpos[1] - (PROW - bpos[0])
    else: # going right
        return bpos[1] + (PROW - bpos[0])

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

num_blocks = 0
grid = [[0 for x in range(MAX_COL+1)] for y in range(MAX_ROW+1)]
print(len(grid), len(grid[0]))
        
vc = Intcode(pgm, 0)
while True:
    c = vc.run()
    if vc.halted:
        break
    r = vc.run()
    if vc.halted:
        break
    tile = vc.run()
    if vc.halted:
        break
    print(r,c,tile)
    grid[r][c] = int(tile)
    if tile == 2:
        num_blocks += 1
    
print('Part 1:', num_blocks)
draw_grid(grid)

print('Part 2:')
vc = Intcode(pgm, 0)
vc.pgm[0] = 2
blocks = set()
last_bpos = None
pcol = 0
score = 0
while True:
    c = vc.run()
    if vc.halted:
        break
    r = vc.run()
    if vc.halted:
        break
    tile = vc.run()
    if vc.halted:
        break
    if c == -1:
        score = tile
        print(f'{score=}')
    else:
        grid[r][c] = int(tile)
        
    if tile == 0 and (r,c) in blocks: # a block is now a space
        blocks.remove((r,c))
        print(f'hit block {r},{c}! {len(blocks)} left.')
    elif tile == 2: # block (only on initial setup)
        blocks.add((r,c))
    elif tile == 3: # save current paddle column
        pcol = c
    elif tile == 4: # track ball and predict the column where it'll hit the paddle
        bpos = (r,c)
        hit_col = predict_hit_col(bpos, last_bpos)
        last_bpos = bpos

        # more paddle towards predicted column
        if pcol > hit_col:
            vc.input = -1
        elif pcol < hit_col:
            vc.input = 1
        else:
            vc.input = 0
            
print('Part 2:', score)
