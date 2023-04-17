def npr (i, n) :
    global cnt
    if n < 500 :
        return
    elif i == N-1 :
        cnt += 1
        return
    else :
        for k in range(N):
            if used[k] == 0 :
                n += kit[k]
                n -= K
                used[k] = 1
                npr(i+1, n)
                used[k] = 0
                n += K
                n -= kit[k]



N, K = map(int, input().split())
kit = list(map(int, input().split()))
cnt = 0
used = [0] * N
npr(0, 500)
print(cnt)