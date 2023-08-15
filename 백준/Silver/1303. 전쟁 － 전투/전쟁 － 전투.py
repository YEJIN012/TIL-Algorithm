import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
arr =[input().strip() for _ in range(M)]

def dfs(si, sj, team, cnt) :
    for di, dj in [(-1,0),(0,1),(1,0),(0,-1)] :
        ni = si + di
        nj = sj + dj
        if 0<=ni<M and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] == team :
            visited[ni][nj] = 1
            cnt = dfs(ni,nj,team,cnt+1) # 재귀에서 되돌아 나올 때에도 동일하게 최대 cnt 값을 return 하기 위해서 cnt 값에 return cnt 를 저장해준다.

            # dfs(ni, nj, team, cnt+1)
            # visited[ni][nj] = 1
            # 이런식으로 빠져나오면 최종 return 되는 cnt는 1이 된다.
    # print(cnt, team)

    return cnt  # 상하좌우에 더이상 방문하지 않은 같은 팀이 없으면, 모여있는 총인원 cnt 반환.

visited = [[0] * N for _ in range(M)]
white = blue = 0
for i in range(M) :
    for j in range(N) :
        if visited[i][j] == 0 :
            if arr[i][j] == 'W' :
                visited[i][j] = 1
                cnt = dfs(i, j, 'W', 1)
                white += cnt ** 2
            else :
                visited[i][j] = 1
                cnt = dfs(i, j, 'B', 1)
                blue += cnt ** 2
print(white, blue)