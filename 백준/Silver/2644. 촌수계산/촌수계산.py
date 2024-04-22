def dfs(a, cnt):
    global flag

    visited[a] = 1

    if a == b:
        flag = 1
        print(cnt)

    for c in adj[a]:
        if not visited[c]:
            dfs(c, cnt + 1)

N = int(input())
a, b = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


visited = [0] * (N+1)
flag = 0

dfs(a, 0)
if not flag:
    print(-1)