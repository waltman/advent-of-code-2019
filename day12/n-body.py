#!/usr/bin/env python3
from sys import argv
import re
import numpy as np
import math

def lcm(x, y):
    return (x * y) // math.gcd(x,y)

def lcm_list(a):
    res = lcm(a[0], a[1])
    for i in range(2, len(a)):
        res = lcm(res, a[i])
    return res

STEPS = 1000
moon_pos = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        m = re.search('=([\-\d]+).*?=([\-\d]+).*?=([\-\d]+)', line)
        moon_pos.append(np.array([int(m.group(i)) for i in range(1,4)]))
moon_vel = [np.zeros(3, 'int') for _ in range(len(moon_pos))]

# save initial state for part 2
init_moon_pos = np.copy(moon_pos)
init_moon_vel = np.copy(moon_vel)

for step in range(1,STEPS+1):
    # get new velocities
    new_vel = [np.copy(x) for x in moon_vel]
    for i in range(len(moon_pos)):
        for j in range(len(moon_pos)):
            for k in range(3):
                if moon_pos[i][k] < moon_pos[j][k]:
                    new_vel[i][k] += 1
                elif moon_pos[i][k] > moon_pos[j][k]:
                    new_vel[i][k] -= 1

    # adjust positions and velocities
    for i in range(len(moon_pos)):
        moon_pos[i] += new_vel[i]
        moon_vel[i] = np.copy(new_vel[i])

# Compute total energy
tot = 0
for i in range(len(moon_pos)):
    pot = sum(abs(x) for x in moon_pos[i])
    kin = sum(abs(x) for x in moon_vel[i])
    tot += pot * kin

print('Part 1', tot)

# Part 2 -- try to find a repeated state

moon_pos = np.copy(init_moon_pos)
moon_vel = np.copy(init_moon_vel)

step = 1
cycle = [None for _ in range(3)]
found = 0
while found < 3:
    # get new velocities
    new_vel = [np.copy(x) for x in moon_vel]
    for i in range(len(moon_pos)):
        for j in range(len(moon_pos)):
            for k in range(3):
                if moon_pos[i][k] < moon_pos[j][k]:
                    new_vel[i][k] += 1
                elif moon_pos[i][k] > moon_pos[j][k]:
                    new_vel[i][k] -= 1

    # adjust positions and velocities
    for i in range(len(moon_pos)):
        moon_pos[i] += new_vel[i]
        moon_vel[i] = np.copy(new_vel[i])

    # look for cycles along each dimension
    for i in range(3):
        if cycle[i] is None:
            match = True
            for j in range(len(moon_pos)):
                if moon_pos[j][i] != init_moon_pos[j][i] or moon_vel[j][i] != init_moon_vel[j][i]:
                    match = False
                    break
            if match:
                cycle[i] = step
                print(i, step, cycle)
                found += 1
    
    step += 1

print(cycle)
print(lcm_list(cycle))
print('Part 2:', lcm_list(cycle))
