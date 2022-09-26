def bfs(i,j) :
    global cnt
    q = [(i,j)]
    while q :
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and field[ni][nj] == 1 :
                q.append((ni,nj))
                field[ni][nj] = 0   # 방문한 배추는 0으로 지워줌.
    cnt += 1                        # 하나의 인접영역이 끝나면, 지렁이 수 +1


for tc in range(1, int(input())+1) :
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K) :
        X, Y = map(int, input().split())    # 열, 행 순으로 입력받음!
        field[Y][X] = 1
    cnt = 0                         # 최소 지렁이 마리 수
    for i in range(N) :
        for j in range(M) :
            if field[i][j] == 1 :   # 배추가 있는 곳부터 순회.
                bfs(i,j)
    print(f'{cnt}')