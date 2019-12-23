import re

# test on the example at https://adventofcode.com/2019/day/17
#s='R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2'
s='L,6,L,4,R,12,L,6,R,12,R,12,L,8,L,6,L,4,R,12,L,6,L,10,L,10,L,6,L,6,R,12,R,12,L,8,L,6,L,4,R,12,L,6,L,10,L,10,L,6,L,6,R,12,R,12,L,8,L,6,L,4,R,12,L,6,L,10,L,10,L,6'

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
#                print(f'{s[start:]}')
#                print(f'{routine=}')
                found = True
                break
        if not found:
#            print(f"couldn't find a pattern in {s[start:]}")
            return
    return routine
            
#print(s)
#print()
start_i = 0
for i in range(start_i+20,start_i+5,-1):
    if not s[i].isdigit():
        continue
    A = s[start_i:i+1]
    start_j = i+2
    while s[start_j:start_j+len(A)] == A:
        start_j += len(A)+1
        print('HIT1')
    for j in range(start_j+20,start_j+5,-1):
        if j >= len(s):
            continue
        if not s[j].isdigit():
            continue
        B = s[start_j:j+1]
        start_k = j+2
        while True:
            if s[start_k:start_k+len(A)] == A:
                start_k += len(A)+1
                print('HIT2')
                continue
            if s[start_k:start_k+len(B)] == B:
                start_k += len(B)+1
                print('HIT3')
                continue
            break
        for k in range(start_k+20,start_k+5,-1):
            if k >= len(s):
                continue
            if not s[k].isdigit():
                continue
            C = s[start_k:k+1]
#            print(0, i, i+2, j, j+2, k, s[0:i+1],s[i+2:j+1],s[j+2:k+1])
#            print(start_i, start_j, start_k, s[start_i:i+1],s[start_j:j+1],s[start_k:k+1])
#            print(s[start_i:i+1],s[start_j:j+1],s[start_k:k+1])
            res = make_routine(s, [s[start_i:i+1],s[start_j:j+1],s[start_k:k+1]])
            if res:
                print(res)
                print(f'{A=} {B=} {C=}')
        

# patterns = []
# start = 0
# for _ in range(3):
#     # does it start with a pattern we've already seen?
#     done = False
#     while not done:
#         for p in patterns:
#             if re.search(f'^{p}', s[start:]):
#                 start += len(p) + 1
#                 break
#         done = True
#     print(s[start:])
#     p = best_match(s[start:])
#     patterns.append(p)
#     print(f'{p=}')
#     print(f'{patterns=}')

#if len(patterns) == 0:
#    patterns.append('')
#print(patterns)
#print(",".join(make_routine(s, patterns)))
