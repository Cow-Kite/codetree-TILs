s, q = input().split()

for _ in range(int(q)):
    n = int(input())
    if n == 1:
        s = s[1:] + s[0]
    elif n==2:
        s = s[-1] + s[:-1]
    elif n==3:
        s = s[-1::-1]
    print(s)