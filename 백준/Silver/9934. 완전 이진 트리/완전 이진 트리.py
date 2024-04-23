def dfs(lst, level):
    midIndex = len(lst) // 2 # 배열의 가운데 인덱스 구하기
    ans[level].append(lst[midIndex])

    if len(lst) == 1: # 종료조건
        return

		# 가운데 인덱스를 기준으로 좌, 우로 나눠서 다시 dfs 돌린다.
    dfs(lst[:midIndex], level + 1)
    dfs(lst[midIndex + 1:], level + 1)

K = int(input()) # level
numList = list(map(int, input().split()))

ans = [[] for _ in range(K)] # 정답을 담을 배열, level의 개수만큼 생성

dfs(numList, 0)

for i in ans:
    print(*i)

