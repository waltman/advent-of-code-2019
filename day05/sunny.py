#!/usr/bin/env python3
from sys import argv

class intcode:
    def __init__(self, pgm):
        self.pgm_init = pgm

    def run(self):
        self.pgm = [x for x in self.pgm_init]
        self.ip = 0
        self.last = 0

        while True:
#            print(f"{self.ip=} {self.pgm[self.ip]=} {self.pgm=}")
            if self.pgm[self.ip] == 1:
                self.do_add()
            elif self.pgm[self.ip] == 2:
                self.do_mult()
            elif self.pgm[self.ip] == 3:
                self.do_input()
            elif self.pgm[self.ip] == 4:
                self.do_output()
            elif self.pgm[self.ip] == 99:
                print("halting")
                break
            else:
                print(f"unknown op {self.pgm[self.ip]}")
        return self.last

    def do_add(self):
        self.pgm[self.pgm[self.ip+3]] = self.pgm[self.pgm[self.ip+1]] + self.pgm[self.pgm[self.ip+2]]
        self.ip += 4

    def do_mult(self):
        self.pgm[self.pgm[self.ip+3]] = self.pgm[self.pgm[self.ip+1]] * self.pgm[self.pgm[self.ip+2]]
        self.ip += 4

    def do_input(self):
#        print("do_input()")
        INPUT = 1
        self.pgm[self.pgm[self.ip+1]] = INPUT
        self.ip += 2

    def do_output(self):
#        print("do_output()")
        print(self.pgm[self.pgm[self.ip+1]])
        self.last = self.pgm[self.pgm[self.ip+1]]
        self.ip += 2

filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

vc = intcode(pgm)
print('Part 1:', vc.run())
