string = []
for _ in range(4):
    string.append(input())
    
for i in range(len(string)-1, -1, -1):
    for j in range(len(string[i])-1, -1, -1):
        print(string[i][j], end="")
    print()