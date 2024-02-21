K = int(input())
N = 2**K - 1
lst = list(map(int, input().split()))
answer = [[] for _ in range(K)]

def dfs(lst, depth):
    mid_idx = len(lst) // 2
    answer[depth].append(lst[mid_idx])

    if len(lst) == 1:
        return

    dfs(lst[:mid_idx], depth+1)
    dfs(lst[mid_idx+1:], depth+1)


dfs(lst, 0)

for i in answer:
    print(*i)