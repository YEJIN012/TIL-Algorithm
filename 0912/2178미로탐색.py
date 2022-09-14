def bfs(N,M) :
    q = []
    visited = [[0] * (M+1) for _ in range(N+1)]
    visited[1][1] = 1
    q.append((1,1))
    while q :
        i, j = q.pop(0)
        if i == N and j == M :
            return visited[i][j]                    # (N,M) 도달시, 경로길이 return
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :
            ni, nj = i + di, j + dj
            if 1<=ni<=N and 1<=nj<=M and arr[ni][nj] != 0 and visited[ni][nj] == 0 :
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return


N, M = map(int, input().split())
arr = [[0] * (M+1)] + [[0] + list(map(int, input())) for _ in range(N)] # (1,1)부터 시작하는 인덱스 통일.

print(bfs(N,M))