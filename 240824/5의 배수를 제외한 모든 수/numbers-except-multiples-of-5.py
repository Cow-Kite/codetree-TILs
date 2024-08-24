x, y = map(int, input().split())

hap = 0 
cnt = 0

for i in range(x, y+1):
    if i % 5 == 0:
        continue
    hap += i
    cnt += 1

if cnt =
print(f'{hap} {hap/cnt:.1f}')