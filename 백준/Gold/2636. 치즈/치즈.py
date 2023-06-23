# 상하좌우 비어있는 칸 따라서 bfs -> 벽에 닿으면 c
N, M = map(int, input().split())    # 행 렬
arr = [[-1] * M] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * M]

def bfs(a, b) :
    q = [(a,b)]
    while q :
        i, j = q.pop()
        for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] :
            ni, nj = i + di, j + dj
            if arr[ni][nj] == -1 :
                return 1

            elif visited[ni][nj] == 0 and arr[ni][nj] == 0 :
                visited[ni][nj] = 1
                q.append((ni,nj))
ans = 0
hour = 0
while True :
        melted = []
        cnt = 0
        for i in range(1, N+1) :
            for j in range(1, M+1) :
                if arr[i][j] == 1 :
                    visited = [[0] * (M + 2) for _ in range(N+2)]
                    visited[i][j] = 1
                    if bfs(i,j) :
                        melted.append((i,j))
                        cnt += 1

        if cnt :
            ans = cnt
            hour += 1
            for a, b in melted :
                arr[a][b] = 0
        else :
            break

print(hour)
print(ans)
