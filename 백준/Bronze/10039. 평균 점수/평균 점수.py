# 10039 평균 점수

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

score_lst = [A, B, C, D, E]

for score in range(len(score_lst)):
    if score_lst[score] < 40:
        score_lst[score] = 40

# print(score_lst)
print(int(sum(score_lst)/5))
