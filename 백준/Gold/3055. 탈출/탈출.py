import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < R and 0 <= nc < C: # maps 범위 내에 있다면
                # 고슴도치가 이동하는 경우
                # 현재 위치가 S이고 이동하려는 위치가 . 이거나 D일 경우
                if maps[r][c] == 'S' and (maps[nr][nc] == '.' or maps[nr][nc] == 'D'):
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                    maps[nr][nc] = 'S'

                # 물이 이동하는 경우
                # 현재 위치가 *이고 이동하려는 위치가 . 또는 S인 경우
                if maps[r][c] == '*' and (maps[nr][nc] == '.' or maps[nr][nc] == 'S'):
                    maps[nr][nc] = '*'
                    q.append((nr, nc)) #

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

visited = [[-1] * C for _ in range(R)]
q = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'D': # 굴의 좌표 구하기
            Di, Dj = i, j

# 고슴도치를 먼저 움직이게 하기 위해서 먼저 큐에 넣어준다.
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            Si, Sj = i, j
            q.append((i, j))
            visited[i][j] = 0 # 출발지점 시간을 0으로 초기화 한다.

# 물의 위치를 모두 찾아 큐에 저장한다.
for i in range(R):
    for j in range(C):
        if maps[i][j] == '*':
            q.append((i, j))

bfs(Si, Sj)

if visited[Di][Dj] != -1:
    print(visited[Di][Dj])
else:
    print('KAKTUS')