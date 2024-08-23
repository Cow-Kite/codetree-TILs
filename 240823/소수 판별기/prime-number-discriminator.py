n = int(input())
sentiment = False
for i in range(1, n):
    if n % i == 0:
        sentiment = True

print('P') if sentiment == True else print('C')