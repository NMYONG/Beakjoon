def dfs(n, lst):
    if n == 3:
        if sum(lst) <= M:
            ans.append(lst)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, lst + [numList[i]])
            visited[i] = 0

N, M = map(int, input().split())
numList = list(map(int, input().split()))

ans = []
visited = [0] * N

dfs(0, [])

max = 0
for i in ans:
    if sum(i) > max:
        max = sum(i)

print(max)
