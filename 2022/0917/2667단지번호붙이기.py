def bfs(i, j) :
    global cnt
    q = [(i,j)]
    visited[i][j] = 1
    homeofapt = 1       # 단지에 속하는 집의 수
    while q :
        i, j = q.pop(0)
        arr[i][j] = 0
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] == 0 :
                q.append((ni,nj))
                visited[ni][nj] = 1
                homeofapt += 1
    cnt += 1
    apt.append(homeofapt)


N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
apt = []                # 단지에 속하는 집의 수 리스트
cnt = 0                 # 단지수
visited = [[0] * N for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 :
            bfs(i, j)
apt = sorted(apt)       # 각 단지에 속하는 집의 수를 오름차순 정렬

print(cnt)
for i in apt :
    print(i)