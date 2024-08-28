s = input()
for _ in range(s):
    s = s[-1] + s[:-2]
    print(s)