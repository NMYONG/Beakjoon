def dfs(start, cnt):
    global flag

    visited[start] = True

    if start == B:
        flag = True
        print(cnt)

    for c in adj[start]:
        if visited[c] == False:
            dfs(c, cnt + 1)


N = int(input())
A, B = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [False for _ in range(N+1)]
flag = False
dfs(A, 0)

if flag == False:
    print(-1)
