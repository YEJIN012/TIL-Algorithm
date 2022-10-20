def f(i, j) :
    for m in range(i,i+8) :
        for n in range(j,j+8) :
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)] :
                ni, nj = m+di, n+dj
                if i<=ni<i+8 and j<=nj<j+8 :
                    if arr[ni][nj] == arr[m][n] :



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        f(0, 0)