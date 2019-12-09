#!/usr/bin/env python3
from sys import argv
from Intcode import Intcode

# read in the program
filename = argv[1]
with open(filename) as f:
    pgm = {i:int(x) for i,x in enumerate(f.readline().rstrip().split(","))}

print(pgm)
