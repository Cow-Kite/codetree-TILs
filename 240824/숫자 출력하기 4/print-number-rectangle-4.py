n, k = map(int, input().split())
if k == 1:
    for i in range(1, n+1):
        print(f'{i} '*n)

if k == 2:
    for i in range(1, n+1):
        if i % 2 == 0:
            for j in range(1, n+1):
                print(f'{j} ')
        else:
            for h in range(n, 0, -1):
                print(f'{h} ')

if k == 3:
    for i in range(1, n+1):
        for j in range(i, i+n+1):
            print(f'{j+1} ')