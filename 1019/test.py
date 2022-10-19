def bfs(i, j) :
    q = [(i,j)]
    visited[i][j] = 1
    d = 0
    sherk = 0
    while q :
        d += 1
        i, j = q.pop(0)
        for di, dj in direction :
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 :
                if case[ni][nj] == 0 :                  # 상어가 없으면
                    visited[ni][nj] = visited[i][j]+1   # i,j 기준으로 거리로 visited 표시
                    q.append((ni,nj))
                else :                                  # 상어가 있으면
                    sherk = 1                           # 탐색 종료.
                    break

        if sherk == 1 :
            break

    return visited[i][j]


N, M = map(int, input().split())
case = [list(map(int,input().split())) for _ in range(N)]
direction = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
maxV = 0
for i in range(N) :
    for j in range(M) :
        if case[i][j] == 0 :    # 상어가 없는 칸에서 모두 bfs탐색
            visited = [[0]*M for _ in range(N)]
            distance = bfs(i, j)
            if maxV < distance :
                maxV = distance
print(maxV)
