# 10156 과자

K, N, M = map(int, input().split())

if K * N <= M:
    print('0')
else :
    print(abs(K * N - M))