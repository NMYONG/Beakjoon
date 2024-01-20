# 10102 개표

V = int(input())
vote = input()

A = 0
B = 0
for i in vote:
    if i == 'A':
        A += 1
    else:
        B += 1

if A > B :
    print('A')
elif A == B :
    print('Tie')
else :
    print('B')