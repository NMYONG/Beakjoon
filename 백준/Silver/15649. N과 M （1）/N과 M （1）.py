def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for j in range(1, N+1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, lst+[j])
            visited[j] = 0

N, M = map(int, input().split())
ans = []
visited = [0] * (N+1)

dfs(0, [])
for lst in ans:
    print(*lst)