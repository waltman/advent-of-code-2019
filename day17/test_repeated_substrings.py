import re

# test on the example at https://adventofcode.com/2019/day/17
s='R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2'

def best_match(s):
    max_str = ''
    max_val = -1
    for i in range(20,6,-1):
        if not re.match('\d', s[i-1]):
            continue
        m = re.findall(s[0:i], s)
        if len(m) > max_val:
            max_val = len(m)
            max_str = s[0:i]

    return max_str

def make_routine(s, patterns):
    name = ['A','B','C']
    routine = []
    start = 0
    while start < len(s):
        for i in range(3):
            if re.search(f'^{patterns[i]}', s[start:]):
                routine.append(name[i])
                start += len(patterns[i])+1
                break
        if i == 3:
            print(f"couldn't find a pattern in {s[start:]}")
            break
    return routine
            

patterns = []
start = 0
for _ in range(3):
    p = best_match(s[start:])
    patterns.append(p)
    start += len(p)+1

print(patterns)
print(",".join(make_routine(s, patterns)))
