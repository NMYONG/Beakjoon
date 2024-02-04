# 2506 점수계산

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
sum_cnt = 0
for i in nums:

    if i == 1:
        cnt += 1
    else:
        cnt = 0
    sum_cnt += cnt

print(sum_cnt)