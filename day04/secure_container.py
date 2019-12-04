import re

def is_sorted(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

n = 0
for i in range(183564, 657474+1):
    s = str(i)
    if is_sorted(s) and re.search('(\d)\\1', s):
        n += 1
print('Part 1:', n)

n = 0
for i in range(183564, 657474+1):
    s = str(i)
    if is_sorted(s):
        # check if there's a pair of adjacent digits
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                try:
                    if s[j] == s[j-1] or s[j] == s[j+2]:
                        continue
                except IndexError:
                    pass
                n += 1
                break
print('Part 2:', n)
