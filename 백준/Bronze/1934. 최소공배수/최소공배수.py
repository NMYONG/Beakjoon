import math

T = int(input())

for test_case in range(T):
    a, b = map(int, input().split())

    GCD = math.gcd(a, b)

    LCM = (a * b) // GCD

    print(LCM)