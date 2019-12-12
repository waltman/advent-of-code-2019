#!/usr/bin/env python3
from sys import argv
import re
import numpy as np

def state_key(moon_pos, moon_vel):
    key = []
    for i in range(len(moon_pos)):
        key += list(moon_pos[i])
        key += list(moon_vel[i])
    return tuple(key)

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
#seen = set(tuple(moon_pos) + tuple(moon_vel))
seen = set()
seen.add(state_key(moon_pos, moon_vel))

step = 1
while True:
    if step % 1000 == 0:
        print(f'{step=}')
        
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

    key = state_key(moon_pos, moon_vel)
    if key not in seen:
        seen.add(key)
        step += 1
    else:
        break

print('Part 2:', step)
