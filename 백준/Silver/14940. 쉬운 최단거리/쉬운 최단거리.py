from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = list([0] * M for _ in range(N))
distance = arr.copy()

def bfs(i, j) :
    q = deque([(i,j)])
    visited[i][j] = 1
    while q :
        i, j = q.popleft()
        for di, dj in [(0,1), (1,0), (0,-1), (-1, 0)] :
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 :
                visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj] != 0 :
                    distance[ni][nj] = visited[ni][nj] - 1
                    q.append((ni,nj))
    for n in range(N) :
        for m in range(M) :
            # 원래 갈 수 있는데 인데 못 갔을 때만 -1
            if arr[n][m] == 1 and visited[n][m] == 0 :
                distance[n][m] = -1

si, sj = (0,0)
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 2 :
            si = i
            sj = j
distance[si][sj] = 0
bfs(si, sj)
for i in range(N) :
    print(" ".join(map(str, distance[i])))
