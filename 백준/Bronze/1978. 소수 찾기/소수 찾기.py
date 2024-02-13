# 1978 소수 찾기

N = int(input())
num_lst = list(map(int, input().split()))

total_cnt = 0
for num in num_lst:
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        total_cnt += 1

print(total_cnt)