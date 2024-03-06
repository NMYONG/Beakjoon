N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]


count = 0

# '-'인 경우
for i in range(N):
    a = ''
    for j in range(M):
        if floor[i][j] == '-' and floor[i][j] != a:
            count += 1
        a = floor[i][j]

for j in range(M):
    a = ''
    for i in range(N):
        if floor[i][j] == '|' and floor[i][j] != a:
            count += 1
        a = floor[i][j]

print(count)