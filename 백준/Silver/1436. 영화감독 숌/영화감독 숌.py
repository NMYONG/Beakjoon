N = int(input())

cnt = 0
num = 666
while True:
    if str(num).count('666') != 0:
        cnt += 1

    if cnt == N:
        break

    num += 1

print(num)