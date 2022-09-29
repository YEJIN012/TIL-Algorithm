def dfs(N) :
    visited = [0] * (10**6+1)
    q = [N]
    while q :
        n = q.pop(0)
        if

N = int(input())
t = bfs(N)
ans = [N]

print(t)
print(*ans)