n = int(input())
string = []
for _ in range(n):
    string.append(input())

A = input()
dap = []
cnt = 0
for elem in string:
    if elem.endswith(A):
        cnt += 1
        dap.append(elem)

print(cnt)
for elem in dap:
    print(elem)