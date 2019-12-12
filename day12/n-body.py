#!/usr/bin/env python3
from sys import argv
import re
import numpy as np

STEPS = 1000
moon_pos = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        m = re.search('=([\-\d]+).*?=([\-\d]+).*?=([\-\d]+)', line)
        moon_pos.append(np.array([int(m.group(i)) for i in range(1,4)]))
moon_vel = [np.zeros(3, 'int') for _ in range(len(moon_pos))]

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

# compute total energy
tot = 0
for i in range(len(moon_pos)):
    pot = sum(abs(x) for x in moon_pos[i])
    kin = sum(abs(x) for x in moon_vel[i])
    tot += pot * kin

print('Part 1', tot)
