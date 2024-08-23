arr = list(map(int, input().split()))

if arr[1] > arr[0] or arr[1] > arr[2]:
    print(1)
else:
    print(0)

if arr[0] == arr[1] == arr[2]:
    print(1)