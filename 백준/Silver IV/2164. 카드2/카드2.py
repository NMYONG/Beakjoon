# 2164 카드2
from collections import deque

N = int(input())
number = deque(range(1, N+1))

while len(number) > 1:
    number.popleft()
    if len(number) > 1:
        number.append(number.popleft())

print(number[0])