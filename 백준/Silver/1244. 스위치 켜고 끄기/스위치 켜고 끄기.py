# 남자가 할 일: n의 배수인 번호를 가진 스위치의 상태를 모두 변경
def man_do(n):
    for i in range(n, N+1, n):
        switch[i] = (switch[i] + 1) % 2


# 여자가 할 일:  n번 스위치의 앞 뒤로 같은 스위치가 최대 일 때, 그 범위의 스위치의 상태를 모두 변경
def woman_do(n):
    switch[n] = (switch[n] + 1) % 2
    s = n - 1
    e = n + 1
    while 0 < s and e <= N:
        if switch[s] == switch[e]:
            switch[s] = (switch[s] + 1) % 2
            switch[e] = (switch[e] + 1) % 2
            s -= 1
            e += 1
        else:
            break


N = int(input())
switch = [-1] + list(map(int, input().split()))

Num = int(input())
for _ in range(Num):
    sex, no = map(int, input().split())
    if sex == 1:
        man_do(no)
    else:
        woman_do(no)

for idx in range(1, N+1):
    print(switch[idx], end=' ')
    if (idx % 20) == 0:
        print()