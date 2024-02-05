# 1977 완전제곱수

M = int(input())
N = int(input())

lst = []
for i in range(1, 101):
    square = i**2

    if M <= square <= N:
        lst.append(square)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
    