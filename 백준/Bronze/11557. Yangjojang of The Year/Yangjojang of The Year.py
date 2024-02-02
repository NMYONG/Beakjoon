# 11557 Yangjojang of The Year

T = int(input())
for tc in range(T):
    N = int(input())

    dict = {}
    for _ in range(N):
        S, L = input().split()
        L = int(L)

        dict[L] = S
        
    print(dict[max(list(dict.keys()))])
