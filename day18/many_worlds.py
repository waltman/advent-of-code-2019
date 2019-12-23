#!/usr/bin/env python3
from sys import argv
from collections import deque
import re

class Grid:
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0

    def add_row(self, row):
        if self.cols == 0:
            self.cols = len(row)
        self.grid.append(list(row))
        self.rows += 1

    def current_pos(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == '@':
                    return r,c

    def visible_keys(self):
        r,c = self.current_pos()
        seen = set()
        queue = deque()
        queue.append((r,c))
        visible = []
        while queue:
            r,c = queue.popleft()
            if (r,c) in seen:
                continue
            seen.add((r,c))
            if self.grid[r][c] >= 'a' and self.grid[r][c] <= 'z':
                visible.append(self.grid[r][c])
                continue
            if re.search('[a-z\.]', self.grid[r-1][c]):
                queue.append((r-1,c))
            if re.search('[a-z\.]', self.grid[r+1][c]):
                queue.append((r+1,c))
            if re.search('[a-z\.]', self.grid[r][c-1]):
                queue.append((r,c-1))
            if re.search('[a-z\.]', self.grid[r][c+1]):
                queue.append((r,c+1))
        return visible

    def get(self, r, c):
        return self.grid[r][c]
    
    def set(self, r, c, v):
        self.grid[r][c] = v
    
    def __str__(self):
        return '\n'.join([''.join(g) for g in self.grid])

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
