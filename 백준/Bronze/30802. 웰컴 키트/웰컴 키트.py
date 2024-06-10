N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

tCount = 0
for i in size:
    if i == 0:
        continue
    elif i <= T:
        tCount += 1
    else:
        tCount += (i + T - 1) // T

print(tCount)
print(N // P, N % P)