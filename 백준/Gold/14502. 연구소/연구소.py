from collections import deque

def bfs(tlst):
    for i, j in tlst:
        arr[i][j] = 1


    q = deque()
    w = [[0] * M for _ in range(N)]
    cnt_zero = cnt - 3 # 남은 0의 개수


    for ti, tj in virus:
        q.append((ti, tj))
        w[ti][tj] = 1

    while q:
        r, c = q.popleft()

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and w[nr][nc] == 0 and arr[nr][nc] == 0:
                q.append((nr, nc))
                w[nr][nc] = 1
                cnt_zero -= 1

    for i, j in tlst:
        arr[i][j] = 0

    return cnt_zero


def dfs(n, tlst):
    global ans

    if n == 3:
        ans = max(ans, bfs(tlst))
        return

    for i in range(cnt):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, tlst + [lst[i]])
            v[i] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))

cnt = len(lst)
v = [0] * cnt
ans = 0

dfs(0, [])

print(ans)