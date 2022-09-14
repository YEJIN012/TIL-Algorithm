import sys
sys.setrecursionlimit(100000)

def dfs(V, E, R) :
    global v                            # 방문 순서.
    visited[R] = v
    v += 1                              # 정점 i의 방문 순서를 출력하기 위해 v값을 키워가며 visited에 기록힌다.
    for i in arr[R] :
        if visited[i] == 0 :            # 방문 안한 인접 정점에 방문.
            dfs(V, E, i)


N, M, R = map(int,input().split())
visited = [0] * (N+1)
arr = [[] for _ in range(N+1)]
for _ in range(M) :
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)                    # 간선을 인접점으로 양쪽 정점에 다 저장.
for i in range(N+1) :
    arr[i] = sorted(arr[i],reverse=True)             # 내림차순으로 방문하기 위해 각 정접의 인접점 sort 사용
# print(arr)
v = 1

dfs(N, M, R)
for i in range(1, N+1) :
    print(visited[i])

# 6 4 1
# 2 3
# 1 4
# 1 5
# 4 6
# [[], [5, 4], [3], [2], [6, 1], [1], [4]]
# 1
# 0
# 0
# 3
# 2
# 4
#96%시발
