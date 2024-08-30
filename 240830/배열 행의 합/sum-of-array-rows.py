arr = []

for _ in range(5):
    arr.append(list(map(int, input().split())))

for i in range(5):
    hap = 0
    for j in range(len(arr[i])):
        hap += arr[i][j]
    print(hap)