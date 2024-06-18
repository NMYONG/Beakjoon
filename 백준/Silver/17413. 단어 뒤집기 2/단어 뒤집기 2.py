import sys
input = sys.stdin.readline

S = input().rstrip()
stack = []
for char in S:
    if char == '<':
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