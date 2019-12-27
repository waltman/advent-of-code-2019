#!/usr/bin/env python3
from sys import argv
import re

N = 10007
cards = [i for i in range(N)]

filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()

        if m := re.match('^deal with increment (\d+)$', line):
            incr = int(m.group(1))
            tmp = [i for i in range(N)]
            for i in range(N):
                tmp[(i * incr) % N] = cards[i]
            cards = tmp
        elif line == 'deal into new stack':
            cards = cards[::-1]
        elif m := re.match('^cut (.*)$', line):
            if (cut := int(m.group(1))) > 0:
                cards = cards[cut:] + cards[0:cut]
            else:
                cards = cards[N+cut:] + cards[0:N+cut]

print('Part 1:', cards.index(2019))
