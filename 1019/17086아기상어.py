def f(i, j) :
    d = 1
    sherk = 0
    while True:
        for di, dj in direction :
            ni, nj = i+d*di, j+d*dj
            if 0<=ni<N and 0<=nj<M :
                if case[ni][nj] == 0 :
                    pass
                else :
                    sherk = 1
                    break
        else :
            d += 1
        if sherk == 1 :
            break

    return d


N, M = map(int, input().split())
case = [list(map(int,input().split())) for _ in range(N)]
direction = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
maxV = 0
for i in range(N) :
    for j in range(M) :
        if case[i][j] == 0 :
            distance = f(i, j)
            if maxV < distance :
                maxi, maxj = i,j
                maxV = distance
print(maxV)
print(maxi,maxj)


