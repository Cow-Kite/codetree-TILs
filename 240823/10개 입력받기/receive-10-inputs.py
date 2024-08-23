arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 0:
        break
    cnt += 1
hap = 0
for i in range(0, cnt):
    hap += arr[i]

print(f'{hap} {hap/cnt:.1f}')