# 2747 피보나치 수

n = int(input())

def fibo(n):

    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(fibo(n))