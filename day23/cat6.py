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

done = False
while not done:
    for i in range(N):
        resp = vcs[i].run()
        if resp == -42:
            continue
        inputs[i].append(resp)
        print(i, inputs[i])
        if len(inputs[i]) == 3:
            dest = inputs[i][0]
            x = inputs[i][1]
            y = inputs[i][2]
            print(i, dest, x, y)
            if dest == 255:
                print('Part 1', y)
                done = True
                break
            inputs[i].clear()
            vcs[dest].input.append(x)
            vcs[dest].input.append(y)

