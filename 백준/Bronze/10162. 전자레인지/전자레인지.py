# 10162 전자레인지

A = 300
B = 60
C = 10

T = int(input())

if T % 10 == 0:
    x = T // A
    y = (T % A) // B
    z = ((T % A) % B) // C
    print(x, y, z)

else:
    print(-1)