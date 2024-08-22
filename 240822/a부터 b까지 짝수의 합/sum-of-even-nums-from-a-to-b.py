a, b = map(int, input().split(" "))
hap = 0
for i in range(a, b):
    if i % 2 == 0:
        hap += i

print(hap)