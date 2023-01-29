N = int(input())
G = [[] for _ in range(N)]
for i in range(N) :
    G[i] = list(map(int,input().split()))

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if G[i][k]+G[k][j] == 2 :
                G[i][j] = 1
for i in range(N) :
    print(*G[i])
