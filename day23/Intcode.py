from collections import defaultdict, deque

class Intcode:
    def __init__(self, pgm, _input):
        self.pgm_init = pgm
        self.input = deque([_input])
        self.addr = _input
        self.halted = False
        self.broken = False
        self.ip = 0
        self.last = 0
        self.rel_base = 0
        self.pgm = defaultdict(int, {k:v for k,v in self.pgm_init.items()})
        self.ops = {
            1: self.do_add,
            2: self.do_mult,
            3: self.do_input,
            4: self.do_output,
            5: self.do_jit,
            6: self.do_jif,
            7: self.do_lt,
            8: self.do_eq,
            9: self.do_rel_base,
            99: self.do_halt,
            }
        self.input_ptr = 0
        self.empty_ctr = 0

    def run(self):
        self.broken = False
        while True:
            opcode = self.pgm[self.ip] % 100
            modes = str(self.pgm[self.ip])[0:-2]
            try:
                self.ops[opcode](modes)
                if self.broken:
                    break
            except KeyError:
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
#        print(f'do_input() {self.addr=} {self.input=}')
        p1, = self.get_params(modes, 1)
        if type(self.input) == list:
            self.pgm[p1] = self.input[self.input_ptr]
            self.input_ptr += 1
        elif type(self.input) == deque:
            if len(self.input) == 0:
                val = -1
                if self.empty_ctr >= 1:
                    self.last = -42
                    self.broken = True
                    self.empty_ctr = 0
                else:
                    self.empty_ctr += 1
            else:
                val = self.input.popleft()
            self.pgm[p1] = val
        else:
            self.pgm[p1] = self.input
        self.ip += 2

    def do_output(self, modes):
        p1, = self.get_params(modes, 1)
        self.last = self.pgm[p1]
        self.broken = True
        self.ip += 2

    def do_rel_base(self, modes):
        p1, = self.get_params(modes, 1)
        self.rel_base += self.pgm[p1]
        self.ip += 2

    def do_halt(self, modes):
        self.broken = True
        self.halted = True
