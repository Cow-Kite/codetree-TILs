n = int(input())
gob = 1
for i in range(1, 10):
    gob *= i
    if gob >= n:
        print(i)
        break