n = int(input())

arr = map(int, input().split())

for i in arr:
    for j in range(1, arr+1):
        if i % j == 0:
            print(j)