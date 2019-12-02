#!/usr/bin/env python3
from sys import argv

def run_intcode(pgm_init, noun, verb):
    pgm = [x for x in pgm_init]
    pgm[1] = noun
    pgm[2] = verb
    ip = 0
    while True:
        if pgm[ip] == 1:
            pgm[pgm[ip+3]] = pgm[pgm[ip+1]] + pgm[pgm[ip+2]]
        elif pgm[ip] == 2:
            pgm[pgm[ip+3]] = pgm[pgm[ip+1]] * pgm[pgm[ip+2]]
        elif pgm[ip] == 99:
            return pgm[0]
        else:
            print(f'Unknown opcode of {pgm[ip]} at position {ip}')
            print(pgm)
            break
        ip += 4
    

filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

print('Part 1:', run_intcode(pgm, 12, 2))

for noun in range(100):
    for verb in range(100):
        if run_intcode(pgm, noun, verb) == 19690720:
            print('Part 2:', 100 * noun + verb)
