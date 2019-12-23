#!/usr/bin/env python3
from sys import argv

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

grid.set(1,5,'.')
grid.set(1,7,'@')
print(grid)
