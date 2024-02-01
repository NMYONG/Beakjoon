# 2576 홀수

odd = []

for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odd.append(num)

if len(odd) != 0:
    print(sum(odd))
    print(min(odd))

else:
    print(-1)