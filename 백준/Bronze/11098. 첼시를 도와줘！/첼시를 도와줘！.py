# 11098 첼시를 도와줘!

T = int(input())

for _ in range(T):
    p = int(input())
    dic = {}
    for _ in range(p):
        C, name = input().split()
        dic[int(C)] = name
        
    print(dic[max(dic)])

