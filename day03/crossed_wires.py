#!/usr/bin/env python3
from sys import argv

def parse_line(s):
    return [(x[0],int(x[1:])) for x in s.rstrip().split(",")]

def wire_path(a):
    path = set()
    pos = 0 + 0j
    delta = { 'L': -1, 'R': 1, 'U': 1j, 'D': -1j }

    for direction, length in a:
        path |= { pos + x * delta[direction] for x in range(1, length+1) }
        pos += length * delta[direction]
    return(path)

def dist_to_p(a, p):
    pos = 0 + 0j
    d = 0
    delta = { 'L': -1, 'R': 1, 'U': 1j, 'D': -1j }

    for direction, length in a:
        for _ in range(length):
            pos += delta[direction]
            d += 1
            if pos == p:
                return d
    return(-1)

filename = argv[1]
with open(filename) as f:
    w1 = parse_line(f.readline())
    w2 = parse_line(f.readline())

s1 = wire_path(w1)
s2 = wire_path(w2)
crosses = s1 & s2
print('Part 1:', min([int(abs(x.real) + abs(x.imag)) for x in crosses]))

print('Part 2:', min([dist_to_p(w1, cross) + dist_to_p(w2, cross) for cross in crosses]))
