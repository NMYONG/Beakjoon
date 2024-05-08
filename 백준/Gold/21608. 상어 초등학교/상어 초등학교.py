N = int(input())
arr = [[-1] * (N + 2)] + [[-1] + [0] * N + [-1] for _ in range(N)] + [[-1] * (N + 2)]
inputList = [list(map(int, input().split())) for _ in range(N * N)]
sortedList = [[0] * 5] + sorted(inputList)

for lst in inputList:
    maxValue = emptyMaxValue = -1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0: continue
            cnt = emptyCnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if arr[ni][nj] in lst:
                    cnt += 1
                if arr[ni][nj] == 0:
                    emptyCnt += 1
            if maxValue < cnt or maxValue == cnt and emptyMaxValue < emptyCnt:
                maxValue, emptyMaxValue = cnt, emptyCnt
                ei, ej = i, j
    arr[ei][ej] = lst[0]

table = [0, 1, 10, 100, 1000]
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        cnt = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if arr[ni][nj] in sortedList[arr[i][j]]:
                cnt += 1
        ans += table[cnt]

print(ans)
