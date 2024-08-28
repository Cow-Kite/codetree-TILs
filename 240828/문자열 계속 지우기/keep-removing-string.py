A = input()
B = input()

while True:
    idx = -1

    candidates = len(A) - len(B) + 1
    for i in range(candidates):
        is_same = True

        for j in range(len(B)):
            if A[i+j] != B[j]:
                is_same = False
                break
        
        if is_same:
            idx = i
            break
    
    if idx == -1:
        break
    
    A = A[:idx] + B[idx+len(B):]

print(A)