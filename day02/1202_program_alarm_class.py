#!/usr/bin/env python3
from sys import argv

class intcode:
    def __init__(self, pgm):
        self.pgm_init = pgm

    def run(self, noun, verb):
        self.pgm = [x for x in self.pgm_init]
        self.pgm[1] = noun
        self.pgm[2] = verb
        self.ip = 0

        while True:
            if self.pgm[self.ip] == 1:
                self.do_add()
            elif self.pgm[self.ip] == 2:
                self.do_mult()
            elif self.pgm[self.ip] == 99:
                break
        return self.pgm[0]

    def do_add(self):
        self.pgm[self.pgm[self.ip+3]] = self.pgm[self.pgm[self.ip+1]] + self.pgm[self.pgm[self.ip+2]]
        self.ip += 4

    def do_mult(self):
        self.pgm[self.pgm[self.ip+3]] = self.pgm[self.pgm[self.ip+1]] * self.pgm[self.pgm[self.ip+2]]
        self.ip += 4

filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

vc = intcode(pgm)
print('Part 1:', vc.run(12, 2))

for noun in range(100):
    for verb in range(100):
        if vc.run(noun, verb) == 19690720:
            print('Part 2:', 100 * noun + verb)
