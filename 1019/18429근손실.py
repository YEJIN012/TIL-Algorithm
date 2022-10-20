def npr(i,power) :
    global cnt
    if i == N :
        cnt += 1

    elif power < 500 :
        return

    else :
        for j in range(i,N) :
            weight[i], weight[j] = weight[j], weight[i]
            npr(i+1,power-K+weight[i])
            weight[i], weight[j] = weight[j], weight[i]

N, K = map(int, input().split())
weight = list(map(int, input().split()))
cnt = 0
npr(0,500)
print(cnt)