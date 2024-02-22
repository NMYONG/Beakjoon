import sys
input = sys.stdin.readline


def possible(r, c):
    for i in range(r):
        if c == visit[i] or abs(i - r) == abs(visit[i] - c):
            return False
    return True


def backtracking(row):
    global cnt
    if row == N:
        cnt += 1

    else:
        for j in range(N):
            visit[row] = j
            if possible(row, j):
                backtracking(row + 1)


N = int(input())
cnt = 0

visit = [0]*N
backtracking(0)

print(cnt)