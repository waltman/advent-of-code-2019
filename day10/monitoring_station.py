#!/usr/bin/env python3
from sys import argv

def dist_from(asteroids, i):
    dists = set()
    for j in range(len(asteroids)):
        if j != i:
            dists.add((asteroids[j][0] - asteroids[i][0],
                       asteroids[j][1] - asteroids[i][1]))
    return dists

def num_visible(asteroids, i):
    MAX = 10
    print('asteroid =', i)
    dists = dist_from(asteroids, i)
    visible = {d for d in dists}
    for d in dists:
        s = set()
        if d[0] == 0: # blocked row
            if d[1] > 0:
                for i in range(d[1]+1, MAX):
                    s.add((0, i))
            else:
                for i in range(d[1]-1, -MAX, -1):
                    s.add((0, i))
        if d[1] == 0: # blocked col
            if d[0] > 0:
                for i in range(d[0]+1, MAX):
                    s.add((i, 0))
            else:
                for i in range(d[0]-1, -MAX, -1):
                    s.add((i, 0))
        for x in range(-6, 7):
            if x == 0 or x == 1:
                continue
            s.add((d[0] * x, d[1] * x))
        visible -= s
    print(len(visible), visible)
    return len(visible)

# parse input
asteroids = []
filename = argv[1]
with open(filename) as f:
    row = 0
    for line in f:
        line = line.rstrip()
        for col in range(len(line)):
            if line[col] == '#':
                asteroids.append((row,col))
        row += 1

print('Part 1:', max([num_visible(asteroids, i) for i in range(len(asteroids))]))
