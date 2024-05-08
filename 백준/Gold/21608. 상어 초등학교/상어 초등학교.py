N = int(input())
# 입력할 배열 생성
# 4방향 순회 시 범위를 벗어난 조건 없애기 위해 -1 테두리에 둘러준다.
arr = [[-1] * (N + 2)] + [[-1] + [0] * N + [-1] for _ in range(N)] + [[-1] * (N + 2)]
inputList = [list(map(int, input().split())) for _ in range(N * N)]
# lookup table
sortedList = [[0] * 5] + sorted(inputList)

# 1. 전체 배열을 순회하면서 arr 빈 자리에 조건에 맞도록 넣어준다.
for lst in inputList:
    maxValue = emptyMaxValue = -1  # count가 0이 될 수 있기 때문에 -1로 초기화
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0: continue  # 비어있지 않으면 continue
            cnt = emptyCnt = 0  # 친구수와 빈 자리를 세줄 변수 초기화
            # 4방향 순회하면서 검사
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if arr[ni][nj] in lst:  # 좋아하는 친구 리스트 안에 있으면
                    cnt += 1
                if arr[ni][nj] == 0:  # 빈칸인 경우
                    emptyCnt += 1
            if maxValue < cnt or maxValue == cnt and emptyMaxValue < emptyCnt:
                maxValue, emptyMaxValue = cnt, emptyCnt
                ei, ej = i, j
    # 모든 위치 확인 후 자리 저장
    arr[ei][ej] = lst[0]

# 2. 점수 계산
table = [0, 1, 10, 100, 1000]
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        cnt = 0  # 네 방향을 순회하며 친한친구의 수 저장
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if arr[ni][nj] in sortedList[arr[i][j]]: # 좋아하는 친구 목록에 있다면
                cnt += 1
        ans += table[cnt]

print(ans)