from collections import deque

# 돌아가면 안 되지만 가장 먼 곳
# 모든 육지에 대해서 bfs 실행?

def bfs(row, col):

    q = deque()
    q.append((row, col))
    visited[row][col] = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == -1 and maps[nr][nc] == 'L':
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1


N, M = map(int, input().split())
maps = [input() for _ in range(N)]

max_v = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            visited = [[-1] * M for _ in range(N)]
            bfs(i, j)

            for a in range(N):
                for b in range(M):
                    if visited[a][b] > max_v:
                        max_v = visited[a][b]

print(max_v)