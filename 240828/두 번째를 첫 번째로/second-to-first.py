s = list(input())

first = s[0]
second = s[1]

for i in range(len(s)):
    if s[i] == second:
        s[i] = first

print(''.join(s))