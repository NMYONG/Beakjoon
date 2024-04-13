def cal(op_lst, num_lst):
    result = num_lst[0]
    for i in range(1, len(num_lst)):
        if op_lst[i - 1] == '+':
            result += num_lst[i]
        elif op_lst[i - 1] == '-':
            result -= num_lst[i]
        elif op_lst[i - 1] == '*':
            result *= num_lst[i]
        elif op_lst[i - 1] == '/':
            if result < 0:
                result = -(abs(result) // num_lst[i])
            else:
                result //= num_lst[i]
    return result

def combination(n, lst):
    global max_num, min_num

    if n == length:
        result = cal(lst, num_lst)
        if result >= max_num:
            max_num = result
        if result <= min_num:
            min_num = result

        comb_lst.append(lst)
        return

    for i in range(length):
        if not visited[i]:
            visited[i] = 1
            combination(n + 1, lst + [operator_lst[i]])
            visited[i] = 0


N = int(input())
num_lst = list(map(int, input().split()))
operator = list(map(int, input().split()))

# 조합 할 연산자 목록 만들기
operator_lst = []
for i in range(4):
    if i == 0:
        for j in range(operator[0]):
            operator_lst.append('+')
    if i == 1:
        for j in range(operator[1]):
            operator_lst.append('-')
    if i == 2:
        for j in range(operator[2]):
            operator_lst.append('*')
    if i == 3:
        for j in range(operator[3]):
            operator_lst.append('/')

length = len(operator_lst)
comb_lst = []
visited = [0] * length

max_num = -float('inf')
min_num = float('inf')

combination(0, [])

# print(comb_lst)

# result_lst = []

# for i in comb_lst:
#     result_lst.append(cal(i, num_lst))

# print(result_lst)
print(max_num)
print(min_num)