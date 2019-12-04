import re

n = 0
for i in range(183564, 657474+1):
    i_str = str(i)
    if re.search('(\d)\\1', i_str) and ''.join(sorted(i_str)) == i_str:
        n += 1
print('Part 1:', n)

n = 0
for i in range(183564, 657474+1):
    s = str(i)
    if ''.join(sorted(s)) == s:
        # check if there's a pair of adjacent digits
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                if j > 0 and s[j] == s[j-1]:
                    continue
                if j < len(s)-2 and s[j] == s[j+2]:
                    continue
                n += 1
                break
print('Part 2:', n)
