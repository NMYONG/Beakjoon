def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return

    # 선택하는 경우
    dfs(n+1, lst+[n])
    # 선택하지 않는 경우
    dfs(n+1, lst)

N, M = map(int, input().split())
ans = []
dfs(1, [])

for i in ans:
    print(*i)