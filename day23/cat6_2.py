#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = defaultdict(int, {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))})

N = 50
vcs = []
for i in range(N):
    vcs.append(Intcode(pgm, i))

inputs = [[] for _ in range(N)]
nat = (-1,-1)
last_y = -1
done = False
while not done:
    idle = True
    for i in range(N):
        resp = vcs[i].run()
        if resp == -42:
            continue
        else:
            idle = False
        inputs[i].append(resp)
        print(i, inputs[i])
        if len(inputs[i]) == 3:
            dest = inputs[i][0]
            x = inputs[i][1]
            y = inputs[i][2]
            print(i, dest, x, y)
            if dest == 255:
                nat = x,y
                print(f'{nat=}')
            else:
                vcs[dest].input.append(x)
                vcs[dest].input.append(y)
            inputs[i].clear()
    if idle:
        print('idle')
        if nat[1] == last_y:
            print('Part 2:', last_y)
            break
        else:
            last_y = nat[1]
            vcs[0].input.append(nat[0])
            vcs[0].input.append(nat[1])
