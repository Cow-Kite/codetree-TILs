str1 = input()
num = len(str1)
if num % 2 != 0:
    num -= 1
print(str1[num::-2])