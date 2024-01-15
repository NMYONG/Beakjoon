# 2476 주사위 게임

T = int(input())

sum_lst = []

for test_case in range(T):
    lst = list(map(int, input().split()))

    if lst[0] == lst[1] == lst[2] :
        sum = 10000 + lst[0] * 1000

    elif (lst[0] == lst[1]) or (lst[1] == lst[2]) or (lst[0] == lst[2]) :
        if lst[0] == lst[1]:
            sum = 1000 + lst[0] * 100
        elif lst[1] == lst[2] :
            sum = 1000 + lst[1] * 100
        else :
            sum = 1000 + lst[0] * 100

    else :
        sum = max(lst) * 100
    # print('sum:', sum)

    sum_lst.append(sum)
    # print('sum_lst:', sum_lst)


print(max(sum_lst))