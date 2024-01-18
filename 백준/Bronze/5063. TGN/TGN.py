# 5062 TGN

T = int(input())
for test_case in range(T):
    # r = 광고를 하지 않았을 때 수익
    # e = 광고를 했을 떄의 수익
    # c = 광고 비용
    r, e, c = map(int, input().split())
    if r < (e - c):
        print('advertise')
    elif r > (e - c):
        print('do not advertise')
    elif r == (e - c):
        print('does not matter')