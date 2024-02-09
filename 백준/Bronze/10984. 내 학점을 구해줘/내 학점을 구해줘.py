# 10984 내 학점을 구해줘

T = int(input())

for tc in range(T):
    N = int(input())

    sum_C = 0
    avg_G = 0
    for n in range(N):
        C, G = map(float, input().split())
        sum_C += C
        avg_G += C * G
    
    GPA = avg_G / sum_C
    print(int(sum_C), '%.1f' % GPA)