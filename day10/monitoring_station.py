#!/usr/bin/env python3
from sys import argv
import math

def sign(x):
    return int(math.copysign(1,x))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# given a vector x,y, returns:
# - the angle in radians (clockwise with 12:00 = 0)
# - eucludian distance from the origin
def xy2pol(x,y):
    theta = math.atan2(x,-y)
    if theta < 0:
        theta = 2 * math.pi + theta
    dist = math.sqrt(x**2 + y**2)
    return theta, dist

def dist_from(asteroids, i):
    dists = set()
    for j in range(len(asteroids)):
        if j != i:
            dists.add((asteroids[j][0] - asteroids[i][0],
                       asteroids[j][1] - asteroids[i][1]))
    return dists

def visible(asteroids, i):
    MAX = 10
    dists = dist_from(asteroids, i)
    visible = {d for d in dists}
    for d in dists:
        s = set()
        if d[0] == 0:
            slope = (0, sign(d[1]))
        elif d[1] == 0:
            slope = (sign(d[0]), 0)
        elif abs(d[0]) > abs(d[1]):
            div = gcd(abs(d[0]), abs(d[1]))
            slope = (d[0] // div, d[1] // div)
        else:
            div = gcd(abs(d[1]), abs(d[0]))
            slope = (d[0] // div, d[1] // div)
        for x in range(1, MAX):
            s.add((d[0] + slope[0]*x, d[1] + slope[1]*x))
                      
        visible -= s
    return visible

def num_visible(asteroids, i):
    return len(visible(asteroids, i))

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

values = [num_visible(asteroids, i) for i in range(len(asteroids))]
max_value = max(values)
max_idx = values.index(max_value)
print('Part 1:', max_value)
positions = []
for i in range(len(asteroids)):
    if i != max_idx:
        dx = asteroids[i][1]-asteroids[max_idx][1]
        dy = asteroids[i][0]-asteroids[max_idx][0]
        theta, dist = xy2pol(dx, dy)
        positions.append((theta, dist, asteroids[i][1], asteroids[i][0]))
positions.sort()

# if in-line, add 2pi
for i in range(0, len(positions)-1):
    for j in range(i+1, len(positions)):
        if positions[j][0] == positions[i][0]:
            positions[j] = (positions[i][0] + 2 * (j-i) * math.pi, positions[j][1], positions[j][2], positions[j][3])
        else:
            break

positions.sort()
print('Part 2:', positions[199][2]*100 + positions[199][3])


