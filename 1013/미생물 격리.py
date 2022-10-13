def move() :
    for k in range(K) :
        if micro[k][3] != -1 :      # 결합되어서 지워진 군집은 direction에 -1로 표시.
            i, j = micro[k][0], micro[k][1]
            di, dj = direction[micro[k][3]]
            ni, nj = i+di, j+dj
            if ni == 0 or ni == N-1 or nj == 0 or nj == N-1 :
                if micro[k][2] // 2 > 0 :
                    micro[k][2] //= 2
                    micro[k][3] = (micro[k][3] + 2) % 4
                    micro[k][0] = ni
                    micro[k][1] = nj
                    arr[ni][nj] = arr[i][j]
                    arr[i][j] = 0
                else :
                    micro[k][3] = -1
                    arr[i][j] = 0

            elif arr[ni][nj] > 0 :
                if arr[ni][nj] > arr[i][j] :
                    for t in range(k) :         # 해당시간에 이미 움지인 군집들과 겹칠 때만, 결합된다.
                        if micro[t][0] == ni and micro[t][1] == nj :
                            micro[t][2] += arr[i][j]
                    arr[i][j] = 0
                    micro[k][3] = -1
                else :
                    arr[ni][nj] += arr[i][j]
                    arr[i][j] = 0
                    for t in range(k) :
                        if micro[t][0] == ni and micro[t][1] == nj :
                            micro[t][3] = -1
                    micro[k][0] = ni
                    micro[k][1] = nj


            else :
                arr[ni][nj] = arr[i][j]
                arr[i][j] = 0
                micro[k][0] = ni
                micro[k][1] = nj



for tc in range(1, int(input())+1) :
    N, M, K = map(int, input().split())
    # arr = [[-1] * N] + [[-1] + [0] * (N - 2) + [-1] for _ in range(N - 2)] + [[-1] * N]
    arr = [[0]*N for _ in range(N)]
    direction = [(-1,0), (0,-1), (1,0), (0,1)]
    micro = []
    for _ in range(K) :
        i, j, n, d = map(int, input().split())
        micro.append([i,j,n,d-1])
        arr[i][j] = n
    while M :
        move()
        M -= 1
    else :
        total = 0
        for k in range(K) :
            if micro[k][3] != -1 :
                total += micro[k][2]
        print(total)





