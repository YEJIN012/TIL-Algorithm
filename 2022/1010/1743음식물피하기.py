import sys
input = sys.stdin.readline
def bfs(i, j) :
    cnt = 1
    q = [(i, j)]
    arr[i][j] = 0
    while q :
        i, j =q.pop(0)
        for di, dj in [[0,1], [1,0], [0,-1],[-1,0]] :
            ni, nj = i+di, j+dj
            if 0<=ni<N+1 and 0<=nj<M+1 and arr[ni][nj] == 1 :
                q.append((ni,nj))
                arr[ni][nj] = 0
                cnt += 1
    else :
        return cnt      # 인접해 있는 큰 음식물 쓰레기의 크기.


N, M, K = map(int, input().split())
arr = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K) :
    i, j = map(int, input().split())
    arr[i][j] = 1           # 떨어진 음식물 위치 '1'로 표시.
cnt_list = set()
for i in range(1,N+1) :
    for j in range(1,M+1) :
        if arr[i][j] == 1 :
            cnt_list.add(bfs(i, j))
print(max(cnt_list))

# cnt_list = set()
# cnt_list.add(bfs(i, j))
# print(max(cnt_list))