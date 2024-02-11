# 9325 얼마?

T = int(input())

for tc in range(T):
    s = int(input())
    N = int(input())

    sum_qp = 0
    for n in range(N):
        q, p = map(int, input().split())
        sum_qp += q * p

    print(s + sum_qp)
