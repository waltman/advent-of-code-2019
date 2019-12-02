#!/usr/bin/env python3
from sys import argv

filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

i = 0
pgm[1] = 12
pgm[2] = 2
while True:
    if pgm[i] == 1:
        pgm[pgm[i+3]] = pgm[pgm[i+1]] + pgm[pgm[i+2]]
    elif pgm[i] == 2:
        pgm[pgm[i+3]] = pgm[pgm[i+1]] * pgm[pgm[i+2]]
    elif pgm[i] == 99:
        break
    else:
        print(f'Unknown opcode of {pgm[i]} at position {i}')
        print(pgm)
        break
    i += 4

print('Part 1:', pgm[0])

