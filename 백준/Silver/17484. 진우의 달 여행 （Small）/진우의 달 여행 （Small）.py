N, M = map(int, input().split())
arr = []
for _ in range(N) :
    arr.append(list(map(int, input().split())))
rotate = [(1,-1),(1,0),(1,1)]

def dfs(i, j, A, pre) :
    global ans
    if i == N-1 :
        ans = min(ans, A)
        return

    for k in range(3) :
        if k != pre :
            ni = i + rotate[k][0]
            nj = j + rotate[k][1]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(ni, nj, A + arr[ni][nj], k)
                visited[ni][nj] = 0

ans = 100*N*M
for j in range(M) :
    visited = [[0] * M for _ in range(N)]
    visited[0][j] = 1
    dfs(0, j, arr[0][j], 3)

print(ans)