S = input() #
stack = []
for char in S:
    if char == '<': # 괄호로 시작되면 지금까지 스택의 문자열을 뒤집어서 출력, 스택에 괄호 넣어주기
        print(''.join(stack[::-1]), end = '')
        stack.clear()
        stack.append(char)
    elif char == '>':
        stack.append(char)
        print(''.join(stack), end = '')
        stack.clear()
    elif char == ' ' and stack[0] != '<':
        print(''.join(stack[::-1]), end = ' ')
        stack.clear()
    else:
        stack.append(char)
print(''.join(stack[::-1]), end = '')