T = int(input())
for tc in range(1, T+1) :
    N , K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    maxV = 0
    for i in range(N) :
        for j in range(N) :
            if