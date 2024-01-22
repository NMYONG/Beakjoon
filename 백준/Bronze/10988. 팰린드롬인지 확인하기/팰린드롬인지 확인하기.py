# 10988 팰린드롬인지 확인하기

string = list(input())

reverse_string = string[::-1]

if string == reverse_string:
    print('1')
else:
    print('0')