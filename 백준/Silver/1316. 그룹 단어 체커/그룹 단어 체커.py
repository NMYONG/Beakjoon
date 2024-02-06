N = int(input())

total_cnt = 0
for _ in range(N):
    S = str(input())

    s_lst = list(set(S))

    s_cnt = [S.count(c) for c in s_lst]

    cnt = 0

    for i in range(len(s_lst)):
        if s_lst[i]*s_cnt[i] in S:
            cnt = 1
        else:
            cnt = 0
            break

    total_cnt += cnt
print(total_cnt)