pp, p = map(int, input().split())

print(pp, p, end=' ')
for i in range(8):
    pp, p = p, pp+p
    print(p%10, end=" ")