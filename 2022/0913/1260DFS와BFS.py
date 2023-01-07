def dfs(N, V) :
    visited = [0] * (N+1)
    v = V
    stack = []
    visited[v] = 1
    print(v, end=' ')
    while True :
        for w in graph[v] :
            if visited[w] == 0 :
                stack.append(v)
                v = w
                print(v, end=' ')
                visited[v] = 1
                break
        else:
            if stack :
                v = stack.pop()
            else :
                break
    print()

def bfs(N, V) :
    q = []
    visited = [0] * (N+1)
    q.append(V)
    visited[V] = 1
    while q :
        v = q.pop(0)
        print(v, end=' ')
        for w in graph[v] :
            if visited[w] == 0 :
                q.append(w)
                visited[w] = 1
    print()




N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1) :
    graph[i] = sorted(graph[i])
dfs(N, V)
bfs(N, V)