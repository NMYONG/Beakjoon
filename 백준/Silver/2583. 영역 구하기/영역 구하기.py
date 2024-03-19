import sys
from collections import deque

input = sys.stdin.readline


# 0인 것들을 순회하면서 최종 0인 것의 개수를 반환
def bfs(row, col):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((row, col))
    arr[row][col] = 1
    cnt = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]
            if 0 <= new_r < N and 0 <= new_c < M and arr[new_r][new_c] == 0:
                q.append((new_r, new_c))
                arr[new_r][new_c] = 1
                cnt += 1

    lst.append(cnt)


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
lst = []

# arr 배열 만들기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):  # 그림이 뒤집어져도 상관 x => 어차피 빈 공간만 BFS 돌리면 됨
        for j in range(x1, x2):
            arr[i][j] = 1

for row in range(N):
    for col in range(M):
        if arr[row][col] == 0:
            bfs(row, col)

lst.sort()
print(len(lst))
print(*lst)