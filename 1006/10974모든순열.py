def npr(i) :

    if i == N :
        print(*P)

    else :
        for j in range(N) :
            if used[j] == 0 :
                used[j] = 1
                P[i] = nums[j]
                npr(i+1)
                used[j] = 0

N = int(input())
nums = list(i for i in range(1, N+1))
used = [0] * N
P = [0] * N
npr(0)

