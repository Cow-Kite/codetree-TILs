arr = list(map(int, input().split()))

if len(arr) == 100:
    max_num = max(arr)
    min_num = min(arr)
else:
    max_num = max(arr[:-1])
    min_num = min(arr[:-1])

print(max_num, min_num)