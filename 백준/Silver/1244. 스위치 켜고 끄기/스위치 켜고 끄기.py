def toggle(no):
    # if switch[no] == 1:
    #     switch[no] = 0
    # else:
    #     switch[no] = 1
    switch[no] = (switch[no] + 1) % 2


def man(no):
    for i in range(no, N + 1, no):
        toggle(i)


def woman(no):
    toggle(no)
    n = no - 1
    m = no + 1
    while n >= 1 and N >= m and switch[n] == switch[m]:
            toggle(n)
            toggle(m)

            n -= 1
            m += 1




N = int(input())
switch = [-100] + list(map(int, input().split()))
num = int(input())

for _ in range(num):
    sex, no = map(int, input().split())

    if sex == 1:
        man(no)
    else:
        woman(no)

# print(*switch[1:])

for idx in range(1, N+1, 20):
    print(*switch[idx:idx+20])