# 2748 피보나치 수 2

T = int(input())
memo = {}

def fibo(N):
    if N < 2:
        return N
    elif N in memo:
        return memo[N]
    else:
        memo[N] = fibo(N-1) + fibo(N-2)
        return memo[N]
    
print(fibo(T))