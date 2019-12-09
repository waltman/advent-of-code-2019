from collections import defaultdict

class Intcode:
    def __init__(self, pgm, _input):
        self.pgm_init = pgm
        self.input = _input
        self.input_cnt = 0
        self.halted = False
        self.ip = 0
        self.last = 0
        self.rel_base = 0
        self.pgm = defaultdict(int)
        for k,v in self.pgm_init.items():
            self.pgm[k] = v

    def run(self):
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
                break
            elif opcode == 5:
                self.do_jit(modes)
            elif opcode == 6:
                self.do_jif(modes)
            elif opcode == 7:
                self.do_lt(modes)
            elif opcode == 8:
                self.do_eq(modes)
            elif opcode == 9:
                self.do_rel_base(modes)
            elif opcode == 99:
                self.halted = True
                break
            else:
                print(f"unknown op {opcode}")
        return self.last

    def get_params(self, modes, length):
        res = []
        for i in range(-1, -(length+1), -1):
            try:
                if modes[i] == '0':
                    res.append(self.pgm[self.ip-i])
                elif modes[i] == '1':
                    res.append(self.ip-i)
                else:
                    res.append(self.rel_base + self.pgm[self.ip-i])
            except IndexError:
                res.append(self.pgm[self.ip-i])
        return tuple(res)

    def do_add(self, modes):
        p1,p2,p3 = self.get_params(modes, 3)
        self.pgm[p3] = self.pgm[p1] + self.pgm[p2]
        self.ip += 4

    def do_mult(self, modes):
        p1,p2,p3 = self.get_params(modes, 3)
        self.pgm[p3] = self.pgm[p1] * self.pgm[p2]
        self.ip += 4

    def do_jit(self, modes):
        p1,p2 = self.get_params(modes, 2)
        if self.pgm[p1] != 0:
            self.ip = self.pgm[p2]
        else:
            self.ip += 3
        
    def do_jif(self, modes):
        p1,p2 = self.get_params(modes, 2)
        if self.pgm[p1] == 0:
            self.ip = self.pgm[p2]
        else:
            self.ip += 3
        
    def do_lt(self, modes):
        p1,p2,p3 = self.get_params(modes, 3)
        self.pgm[p3] = 1 if self.pgm[p1] < self.pgm[p2] else 0
        self.ip += 4

    def do_eq(self, modes):
        p1,p2,p3 = self.get_params(modes, 3)
        self.pgm[p3] = 1 if self.pgm[p1] == self.pgm[p2] else 0
        self.ip += 4

    def do_input(self, modes):
        p1, = self.get_params(modes, 1)
        self.pgm[p1] = self.input
        self.ip += 2

    def do_output(self, modes):
        p1, = self.get_params(modes, 1)
        self.last = self.pgm[p1]
        self.ip += 2

    def do_rel_base(self, modes):
        p1, = self.get_params(modes, 1)
        self.rel_base += self.pgm[p1]
        self.ip += 2
