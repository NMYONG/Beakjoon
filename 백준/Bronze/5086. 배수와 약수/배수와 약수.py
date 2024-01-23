# 5086 배수와 약수

num1, num2 = map(int, input().split())

while (num1 != 0) and (num2 != 0):
    if num2 % num1 == 0:
        print('factor')
        num1, num2 = map(int, input().split())

    elif num1 % num2 == 0:
        print('multiple')
        num1, num2 = map(int, input().split())

    else:
        print('neither')
        num1, num2 = map(int, input().split())

