
price_sum = int(input())

remain_sum = 0
for _ in range(9):
    a = int(input())
    remain_sum += a

print(price_sum - remain_sum)