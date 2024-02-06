# 5635 생일

T = int(input())

dic = {}
for tc in range(T):
    name, dd, mm, yyyy = input().split()
    day = (30-int(dd)) + (12-int(mm))*30 + (2000-int(yyyy))*12*30

    dic[name] = day

print(min(dic, key=dic.get))
print(max(dic, key=dic.get))
