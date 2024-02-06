# 색종이 수
n = int(input())

# 좌표 생성
board = [[0]*100 for _ in range(100)]

for _ in range(n):
    # 색종이를 붙일 좌표
    a, b = map(int, input().split())

    for i in range(10):
        for j in range(10):
            board[i+a][j+b] += 1

cnt = 0
for k in range(2, 101):
    for i in range(100):
        for j in range(100):
            if k == board[i][j]:
                cnt += k-1

print(n*100-cnt)