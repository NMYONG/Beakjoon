# 10886 0 = not cute / 1 = cute

N = int(input())

one = 0
zero = 0

for test_case in range(N):
    zero_one = int(input())
    if zero_one == 1 :
        one += 1
    else:
        zero += 1

if one > zero :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')
        
# print(one, zero)