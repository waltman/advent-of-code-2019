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
            opcode = self.pgm[self.ip] % 100
            modes = str(self.pgm[self.ip])[0:-2]
            if opcode == 1:
                self.do_add(modes)
            elif opcode == 2:
                self.do_mult(modes)
            elif opcode == 3:
                self.do_input(modes)
            elif opcode == 4:
                self.do_output(modes)
            elif opcode == 99:
                print("halting")
                break
            else:
                print(f"unknown op {opcode}")
        return self.last

    def get_params(self, modes, length):
        res = []
        for i in range(-1, -(length+1), -1):
            try:
                if modes[i] == '0':
                    res.append(0)
                else:
                    res.append(1)
            except IndexError:
                res.append(0)
        return res

    def do_add(self, modes):
        params = self.get_params(modes, 3)
        p1 = self.pgm[self.pgm[self.ip+1]] if params[0] == 0 else self.pgm[self.ip+1]
        p2 = self.pgm[self.pgm[self.ip+2]] if params[1] == 0 else self.pgm[self.ip+2]
        if params[2] == 0:
            self.pgm[self.pgm[self.ip+3]] = p1 + p2
        else:
            self.pgm[self.ip+3] = p1 + p2
        self.ip += 4

    def do_mult(self, modes):
        params = self.get_params(modes, 3)
        p1 = self.pgm[self.pgm[self.ip+1]] if params[0] == 0 else self.pgm[self.ip+1]
        p2 = self.pgm[self.pgm[self.ip+2]] if params[1] == 0 else self.pgm[self.ip+2]
        if params[2] == 0:
            self.pgm[self.pgm[self.ip+3]] = p1 * p2
        else:
            self.pgm[self.ip+3] = p1 * p2
        self.ip += 4

    def do_input(self, modes):
        params = self.get_params(modes, 1)
        INPUT = 1
        if params[0] == 0:
            self.pgm[self.pgm[self.ip+1]] = INPUT
        else:
            self.pgm[self.ip+1] = INPUT
        self.ip += 2

    def do_output(self, modes):
        params = self.get_params(modes, 1)
        if params[0] == 0:
            print(self.pgm[self.pgm[self.ip+1]])
            self.last = self.pgm[self.pgm[self.ip+1]]
        else:
            print(self.pgm[self.ip+1])
            self.last = self.pgm[self.ip+1]
        self.ip += 2

filename = argv[1]
with open(filename) as f:
    pgm = [int(x) for x in f.readline().rstrip().split(",")]

vc = intcode(pgm)
print('Part 1:', vc.run())
