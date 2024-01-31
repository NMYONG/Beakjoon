# 2441 별 찍기

n = int(input())
empt = ' '
star = '*'
for i in range(n, 0, -1):
    print(f'{empt*(n-i)}{star*i}')