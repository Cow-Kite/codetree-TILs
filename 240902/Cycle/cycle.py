N, P = map(int, input().split())

dap = [N, ]
num = N
#cnt = 0
while True:
    num = (num*N)%P
    if num in dap:
        break
    dap.append(num)
    #cnt += 1

print(len(dap)-1)