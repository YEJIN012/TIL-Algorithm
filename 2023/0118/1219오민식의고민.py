import sys
import heapq
input = sys.stdin.readline
INF = int(-1e9)

def dfs(n, end) :
    if n == end :
        return 1
    else :
        for b, c in graph[n] :
            if visited[b] == 0 :
                visited[b] = 1
                dfs(b, end)

def bell(n) :




N, start, end, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
money = [INF] * (N+1)
for _ in range(M) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
earn = list(map(int, input().split()))

ans = ''
visited = [0] * (N+1)
b = dfs(start, end)
if b == -1 :
    ans = 'gg'
elif bell(start) == -1 :
    ans = 'Gee'
else :
    ans = money[end]

print(ans)