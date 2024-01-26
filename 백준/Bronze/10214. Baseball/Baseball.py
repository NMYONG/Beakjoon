# 10214 Baseball

T = int(input())

for test_case in range(T):
    sum_Y = 0
    sum_K = 0

    for i in range(9):
        y, k = map(int, input().split())
        sum_Y += y
        sum_K += k

    if sum_Y > sum_K:
        print('Yonsei')
    elif sum_Y < sum_K:
        print('Korea')
    else:
        print('Draw')