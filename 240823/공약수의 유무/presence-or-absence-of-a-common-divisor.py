a, b = map(int, input().split(" "))
sentiment = False
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        sentiment = True

print(1) if sentiment==True else print(0)