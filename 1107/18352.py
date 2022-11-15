import sys
input = sys.stdin.readline

def bfs(s) :
    q = [s]
    visited[s] = 0
    while q :
        i = q.pop(0)
        for m in node[i] :
            if visited[m] == -1 :
                q.append(m)
                visited[m] = visited[i] + 1
        if visited[i] == K :
            break


N, M, K, X = map(int,input().split())
node = list([] for _ in range(N+1))
for i in range(M) :
    a, b = map(int, input().split())
    node[a].append(b)
visited= [-1] * (N+1)
q = [X]
bfs(X)

for i in range(1, N+1) :
    if visited[i] == K :
        print(i)
if K not in visited :
    print(-1)