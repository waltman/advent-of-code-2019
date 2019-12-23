import re

# test on the example at https://adventofcode.com/2019/day/17
s='R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2'
#s='L,6,L,4,R,12,L,6,R,12,R,12,L,8,L,6,L,4,R,12,L,6,L,10,L,10,L,6,L,6,R,12,R,12,L,8,L,6,L,4,R,12,L,6,L,10,L,10,L,6,L,6,R,12,R,12,L,8,L,6,L,4,R,12,L,6,L,10,L,10,L,6'

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
        found = False
        for i in range(len(patterns)):
            if re.search(f'^{patterns[i]}', s[start:]):
                routine.append(name[i])
                start += len(patterns[i])+1
                print(f'{s[start:]}')
                print(f'{routine=}')
                found = True
                break
        if not found:
            print(f"couldn't find a pattern in {s[start:]}")
            break
    return routine
            

patterns = []
start = 0
for _ in range(3):
    # does it start with a pattern we've already seen?
    done = False
    while not done:
        for p in patterns:
            if re.search(f'^{p}', s[start:]):
                start += len(p) + 1
                break
        done = True
    print(s[start:])
    p = best_match(s[start:])
    patterns.append(p)
    print(f'{p=}')
    print(f'{patterns=}')

#if len(patterns) == 0:
#    patterns.append('')
print(patterns)
print(",".join(make_routine(s, patterns)))
