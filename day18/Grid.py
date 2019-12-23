from collections import deque
import re

class Grid:
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.pos_of = dict()

    def add_row(self, row):
        if self.cols == 0:
            self.cols = len(row)
        self.grid.append(list(row))
        self.rows += 1
        for c in range(self.cols):
            if re.search('[a-zA-Z@]', self.grid[self.rows-1][c]):
                self.pos_of[self.grid[self.rows-1][c]] = (self.rows-1,c)

    def current_pos(self):
        return self.pos_of['@']

    def change_current_pos(self, r, c):
        r1, c1 = self.pos_of['@']
        self.grid[r1][c1] = '.'
        self.grid[r][c] = '@'
        self.pos_of['@'] = (r,c)

    def remove(self, ch):
        r,c = self.pos_of[ch]
        self.grid[r][c] = '.'
        del self.pos_of[ch]

    def visible_keys(self):
        r,c = self.current_pos()
        seen = set()
        queue = deque()
        queue.append((r,c,0))
        visible = []
        while queue:
            r,c,d = queue.popleft()
            if (r,c) in seen:
                continue
            seen.add((r,c))
            if self.grid[r][c] >= 'a' and self.grid[r][c] <= 'z':
                visible.append((self.grid[r][c],d))
                continue
            if re.search('[a-z\.]', self.grid[r-1][c]):
                queue.append((r-1,c,d+1))
            if re.search('[a-z\.]', self.grid[r+1][c]):
                queue.append((r+1,c,d+1))
            if re.search('[a-z\.]', self.grid[r][c-1]):
                queue.append((r,c-1,d+1))
            if re.search('[a-z\.]', self.grid[r][c+1]):
                queue.append((r,c+1,d+1))
        return visible

    def get(self, r, c):
        return self.grid[r][c]
    
    def set(self, r, c, v):
        self.grid[r][c] = v
    
    def __str__(self):
        return '\n'.join([''.join(g) for g in self.grid])
