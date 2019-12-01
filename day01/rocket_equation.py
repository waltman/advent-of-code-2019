#!/usr/bin/env python3
from sys import argv

def fuel_req(n):
    return int(n/3) - 2

def fuel_req_tot(n):
    res = fuel_req(n)
    return 0 if res <= 0 else res + fuel_req_tot(res)

total = 0
total2 = 0
filename = argv[1]
with open(filename) as f:
    for line in f:
        n = int(line.rstrip())
        total += fuel_req(n)
        total2 += fuel_req_tot(n)

print('part 1:', total)
print('part 2:', total2)
