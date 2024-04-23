def dfs(lst, level):
    midIndex = len(lst) // 2
    ans[level].append(lst[midIndex])

    if len(lst) == 1:
        return

    dfs(lst[:midIndex], level + 1)
    dfs(lst[midIndex + 1:], level + 1)

K = int(input()) # level
numList = list(map(int, input().split()))

ans = [[] for _ in range(K)]

dfs(numList, 0)

for i in ans:
    print(*i)

