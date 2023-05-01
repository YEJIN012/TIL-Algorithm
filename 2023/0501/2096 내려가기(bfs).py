N = int(input())
arr = list(list(map(int,input().split(' '))) for _ in range(N))

def bfsMax(i,j) :
    q = [(i, j)]
    visited_max[i][j] = arr[i][j]
    while q:
        i, j = q.pop(0)
        for di, dj in [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
            if 0 <= di < N and 0 <= dj < N :
                if visited_max[di][dj] < visited_max[i][j] + arr[di][dj] :
                    visited_max[di][dj] = visited_max[i][j] + arr[di][dj]
                q.append((di,dj))

def bfsMin(i,j) :
    q = [(i, j)]
    visited_min[i][j] = arr[i][j]
    while q:
        i, j = q.pop(0)
        for di, dj in [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
            if 0 <= di < N and 0 <= dj < N :
                if visited_min[di][dj] > visited_min[i][j] + arr[di][dj] :
                    visited_min[di][dj] = visited_min[i][j] + arr[di][dj]
                q.append((di,dj))

INF = 10*3*(10**5)

visited_max = [[0] * N for _ in range(N)]
visited_min = [[INF] * N for _ in range(N)]
for i in range(N) :
    bfsMax(0, i)
    bfsMin(0, i)

print(max(visited_max[N-1]),min(visited_min[N-1]))
# 메모리초과