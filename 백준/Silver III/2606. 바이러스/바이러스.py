# 2606 바이러스

N = int(input())
l = int(input())
G = [[] for _ in range(N+1)]
cnt = 0

def dfs(start):
    global cnt
    STACK = []
    visited = [False] * (N+1)

    STACK.append(start)
    visited[start] = True

    while STACK:
        v = STACK.pop()

        for w in G[v]:
            if not visited[w]:
                STACK.append(w)
                visited[w] = True
                cnt += 1

    return cnt


for _ in range(l):
    a, b = map(int, input().split())
    v1 = a
    v2 = b

    G[v1].append(v2)
    G[v2].append(v1)

# print(G)
print(dfs(1))
