# 10833 사과

T = int(input())

ab_mod = 0

for tc in range(T):
    A, B = map(int, input().split())
    ab_mod += B % A
    
print(ab_mod)