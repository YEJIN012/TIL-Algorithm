def move() :
    for k in range(K) :
        m = micro
        if micro[k][3] != -1 :      # 결합되어서 지워진 군집은 direction에 -1로 표시.
            i, j = micro[k][0], micro[k][1]
            di, dj = direction[micro[k][3]]
            ni, nj = i+di, j+dj
            if ni == 0 or ni == N-1 or nj == 0 or nj == N-1 :   # 약품 접근시,
                if micro[k][2] > 1 :
                    micro[k][2] //= 2                           # 반으로 반감.
                    if micro[k][3] == 0 or micro[k][3] == 2 :
                        micro[k][3] += 1
                    else :                                      # 또는 미생물수가 1이면, 소멸.
                        micro[k][3] -= 1
                    micro[k][0] = ni
                    micro[k][1] = nj
                else :
                    micro[k][3] = -1

            else :                                              # 그 외에는 일반적으로, 이동.
                micro[k][0] = ni
                micro[k][1] = nj

    for k in range(K) :                                         # 모든 미생물 이동후, 한 셀에 모이는 경우 고려.
        gather_n = [micro[k][2]]                                # 같은 셀에 모이는 군집의 미생물 수 리스트
        gather_k = [k]                                          # 같은 셀에 모이는 군집의 미생물 고유번호 리스트
        if micro[k][3] != -1 :
            for kk in range(k+1, K) :
                if micro[kk][3] != -1:
                    if kk != k :
                        if micro[k][0] == micro[kk][0] and micro[k][1] == micro[kk][1] :
                            gather_k.append(kk)
                            gather_n.append(micro[kk][2])
            if len(gather_k) > 1 :                              # 같은 셀에 모이는 군집들이 있으면,
                s = gather_n.index(max(gather_n))
                micro[gather_k[s]][2] = sum(gather_n)           # 미생물수가 최대인 군집만 미생물 수의 합으로 살리고
                for i in range(len(gather_k)) :
                    if i != s :
                        micro[gather_k[i]][3] = -1              # 나머지는 다 소멸.




for tc in range(1, int(input())+1) :
    N, M, K = map(int, input().split())
    # arr = [[-1] * N] + [[-1] + [0] * (N - 2) + [-1] for _ in range(N - 2)] + [[-1] * N]
    # arr = [[0]*N for _ in range(N)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    micro = []
    for k in range(K) :
        i, j, n, d = map(int, input().split())
        micro.append([i,j,n,d-1])
    while M :
        move()
        M -= 1
    else :
        total = 0
        for k in range(K) :
            if micro[k][3] != -1 :
                total += micro[k][2]
        print(f'#{tc} {total}')