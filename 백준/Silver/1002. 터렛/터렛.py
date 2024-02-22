T = int(input())

import math

for t in range (T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    length1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
    length2 = r1+r2
    if length1 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif length1 < length2:
        if r1+length1 < r2 or r2+length1 < r1:
            print(0)
        elif r1+length1 == r2 or r2+length1 == r1:
            print(1)
        else :
            print(2)
    elif length1 == length2:
        print(1)
    else:
        print(0)