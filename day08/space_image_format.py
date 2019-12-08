#!/usr/bin/env python3
from sys import argv

filename = argv[1]
with open(filename) as f:
    a = [int(x) for x in list(f.read().rstrip())]

# STRIDE = 6
STRIDE = 25 * 6
counts = [a[start:start+STRIDE].count(0) for start in range(0, len(a), STRIDE)]
idx = counts.index(min(counts)) * STRIDE
layer = a[idx:idx+STRIDE]
print('Part 1:', layer.count(1) * layer.count(2))

