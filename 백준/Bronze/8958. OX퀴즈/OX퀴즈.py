# 8958 OX퀴즈

T = int(input())

for test_case in range(T):
    string = input()
    score = 0
    sum_score = 0

    for str in string:
        if str == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

