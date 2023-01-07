def bfs(i, j, N) :
    q = []
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    q.append((i,j))
    while q :
        i, j = q.pop(0)
        if arr[i][j] == -1 :            # -1에 도달시, 도달 가능.
            return "HaruHaru"
        for di, dj in [[1,0],[0,1]] :
            ni, nj = i + di * arr[i][j], j + dj * arr[i][j]     # 칸에 쓰여진 수만큼 오른쪽/아래로 칸을 후보군으로 q에 push
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                q.append((ni,nj))
                visited[ni][nj] = 1
    return "Hing"                       # q가 비어 있을 때까지 다 돌았으면, 도달 불가능.


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(0, 0, N))
