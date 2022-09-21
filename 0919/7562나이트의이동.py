def bfs(i, j) :
    direction = [[-2,1],[-1,2],[1,2],[2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
    q = [(i, j)]
    visited[i][j] = 1                   # 현재 위치를 1로 방문표시
    while q :
        i, j = q.pop(0)
        if i == c and j == d :          # 현위치가 이동하려는 칸이면,
            return visited[i][j] - 1    # 현위치 방문표시 - 1 (=이동횟수) 출력.
        else :
            for di, dj in direction :
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1     # 방문표시를 키워가며 기록.



for tc in range(1, int(input())+1) :
    N = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited = [[0]*N for _ in range(N)]

    print(bfs(a, b))
