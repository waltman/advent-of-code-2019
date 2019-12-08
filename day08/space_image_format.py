#!/usr/bin/env python3
from sys import argv
import numpy as np

filename = argv[1]
with open(filename) as f:
    a = [int(x) for x in list(f.read().rstrip())]

# STRIDE = 6
#STRIDE = 4
ROWS = 6
COLS = 25
STRIDE = ROWS * COLS
counts = [a[start:start+STRIDE].count(0) for start in range(0, len(a), STRIDE)]
idx = counts.index(min(counts)) * STRIDE
layer = a[idx:idx+STRIDE]
print('Part 1:', layer.count(1) * layer.count(2))

layers = len(a) // ROWS // COLS
stack = np.array(a).reshape(layers, ROWS, COLS)

output = np.zeros([ROWS,COLS]).astype(int) - 1
for z in range(layers):
    for r in range(ROWS):
        for c in range(COLS):
            if output[r,c] == -1 and stack[z,r,c] != 2:
                output[r,c] = stack[z,r,c]

# now let's turn output into something more visible
s = ''
for r in range(ROWS):
    for c in range(COLS):
        s += ' ' if output[r,c] == 0 else '*'
    s += '\n'

print('Part 2')
print(output)
print(s)
