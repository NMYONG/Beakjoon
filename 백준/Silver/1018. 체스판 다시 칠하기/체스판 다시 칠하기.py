N, M = map(int, input().split())
chess = [input() for _ in range(N)]

white = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
black = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

min_v = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        # 0, 0이 흰색으로 시작하는 경우에 대해
        case_white = 0
        # 0, 0이 검은색으로 시작하는 경우에 대해
        case_black = 0

        for a in range(8):
            for b in range(8):
                if chess[i + a][j + b] != white[a][b]:
                    case_white += 1
                if chess[i + a][j + b] != black[a][b]:
                    case_black += 1

        min_v = min(min_v, case_white, case_black)

print(min_v)