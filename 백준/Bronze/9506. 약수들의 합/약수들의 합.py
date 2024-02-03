# 9506 약수들의 합

while True:
    num = int(input())
    if num == -1:
        break

    lst = []
    for i in range(1, num+1):
        if num % i == 0:
            lst.append(i)
    if sum(lst[:-1]) == num:
            print(f'{num} = {" + ".join(map(str, lst[:-1]))}')
    else:
        print(f'{num} is NOT perfect.')

    