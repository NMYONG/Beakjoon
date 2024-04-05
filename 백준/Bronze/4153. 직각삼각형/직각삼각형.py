while True:
    lst = sorted(list(map(int, input().split())))

    if not sum(lst):
        break
    else:
        if lst[0]**2 + lst[1]**2 == lst[2]**2:
            print('right')
        else:
            print('wrong')