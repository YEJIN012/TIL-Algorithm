# 플로이드-워셜
INF = int(1e9)
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 워셜 점화식 -> ij 이동 최단거리 2차원배열
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# K에서 시작하는 최단거리를 찾기위한 dfs
def dfs(k, t) :
    global minT
    if sum(visited) == N :
        if t < minT :
            minT = t
            return

    else :
        for i in range(N) :
            if visited[i] == 0 :
                visited[i] = 1
                t += graph[k][i]
                dfs(i, t)
                visited[i] = 0
                t -= graph[k][i]

minT = INF
visited = [0] * N
visited[K] = 1
dfs(K, 0)
print(minT)
