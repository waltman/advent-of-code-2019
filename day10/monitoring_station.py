#!/usr/bin/env python3
from sys import argv
import math

def sign(x):
    return int(math.copysign(1,x))

# given a vector x,y, returns:
# - the angle in radians (clockwise with 12:00 = 0)
# - eucludian distance from the origin
def xy2pol(x,y):
    theta = math.atan2(x,-y)
    if theta < 0:
        theta = math.tau + theta
    dist = math.sqrt(x**2 + y**2)
    return theta, dist

# make an array of (dx,dy) tuples
def dist_from(asteroids, i):
    dists = set()
    for j in range(len(asteroids)):
        if j != i:
            dists.add((asteroids[j][0] - asteroids[i][0],
                       asteroids[j][1] - asteroids[i][1]))
    return dists

# return a list of all the asteroids visible from asteroid i
def visible(asteroids, i):
    MAX = 10 # I'm not really sure this will work in general but it does for me
    dists = dist_from(asteroids, i)
    visible = {d for d in dists}
    for d in dists:
        s = set()
        if d[0] == 0:
            slope = (0, sign(d[1]))
        elif d[1] == 0:
            slope = (sign(d[0]), 0)
        else:
            div = math.gcd(abs(d[1]), abs(d[0]))
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

# For part 2 we'll construct an array of tuples, one for each asteroid that's
# not the monitoring station. The tuple contains:
# (angle, distance, x, y)
# This way we can sort the tuples into the proper order.
positions = []
for i in range(len(asteroids)):
    if i != max_idx:
        dx = asteroids[i][1]-asteroids[max_idx][1]
        dy = asteroids[i][0]-asteroids[max_idx][0]
        theta, dist = xy2pol(dx, dy)
        positions.append((theta, dist, asteroids[i][1], asteroids[i][0]))
positions.sort()

# Now adjust the tuples so that if they're at the same angle, we'll put each
# after the first 2 pi after the prior one, then sort again. That gives us
# the array in vaporizing order.
for i in range(0, len(positions)-1):
    for j in range(i+1, len(positions)):
        if positions[j][0] == positions[i][0]:
            positions[j] = (positions[i][0] + (j-i) * math.tau, positions[j][1], positions[j][2], positions[j][3])
        else:
            break
positions.sort()

# Now that it's sorted we can just pluck off the 200th asteroid
print('Part 2:', positions[199][2]*100 + positions[199][3])


