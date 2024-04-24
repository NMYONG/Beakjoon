import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# print(adj)

def dfs(v):
    for i in adj[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

dfs(1)

for j in range(2, len(visited)):
    print(visited[j])