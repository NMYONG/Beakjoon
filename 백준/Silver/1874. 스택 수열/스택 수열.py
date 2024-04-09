cnt = 1
stack = []
ans = []

N = int(input())

for _ in range(N):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        print('NO')
        exit()

for i in ans:
    print(i)