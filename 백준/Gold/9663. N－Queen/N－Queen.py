import sys
input = sys.stdin.readline

def possible(row, col):
    for r in range(row):
        if board[r] == col or abs(row - r) == abs(col - board[r]):
            return False
    return True

def backtracking(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if possible(row, col):
            board[row] = col
            backtracking(row + 1)

N = int(input())
cnt = 0
board = [-1] * N
backtracking(0)
print(cnt)
