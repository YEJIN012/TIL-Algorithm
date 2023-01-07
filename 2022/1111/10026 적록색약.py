# 적록색약이 아닌 사람의 구역 나누기
def noredgreen(i, j) :
    q = [(i, j)]
    visited[i][j] = 1
    while q :
        i, j = q.pop(0)
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)] :
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] == arr[i][j] :
                visited[ni][nj] = 1
                q.append((ni,nj))

# 적록색약인 사람의 구역 나누기
def redgreen(i, j) :
    q = [(i, j)]
    visited[i][j] = 1
    while q :
        i, j = q.pop(0)
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)] :
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                # R과 G 구분 못함.
                if arr[i][j] == 'R' or arr[i][j] == 'G' :
                    if arr[ni][nj] == 'R' or arr[ni][nj] == 'G' :
                        visited[ni][nj] = 1
                        q.append((ni,nj))
                elif arr[i][j] == 'B' :
                    if arr[i][j] == arr[ni][nj] :
                        visited[ni][nj] = 1
                        q.append((ni, nj))


N = int(input())
arr = list(input() for _ in range(N))
visited=[[0]*N for _ in range(N)]
norg = 0    # 적록색약 아닌 사람의 구역 수
rg = 0      # 적록색약인 사람의 구역수

# 전체 탐색 2번
while True :
    flag = 0
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 : # 구역에 포함되지 않은 칸이면
                noredgreen(i,j)     # 상하좌우 탐색 bfs 실행
                norg += 1           # bfs가 한번 끝나면 구역 종료. 구역 +1
                flag = 1
                break
        if flag == 1:
            break                   # 다시 0,0배열부터 구역에 포함되지 않은 칸 찾기
    else :
        break

visited=[[0]*N for _ in range(N)]
while True :
    flag = 0
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                redgreen(i,j)
                rg += 1
                flag = 1
                break
        if flag == 1:
            break
    else :
        break

print(norg, end=" ")
print(rg)

