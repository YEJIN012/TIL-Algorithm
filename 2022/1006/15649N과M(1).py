# 순열로 배운 코드인데
# 이 코드 자체가 dfs라고 생각해볼수도 있음!!
def dfs(i) :

    if i == M :
        print(*P)

    else :
        for j in range(N) :
            if used[j] == 0 :
                used[j] = 1
                P[i] = nums[j]
                dfs(i+1)
                used[j] = 0


N, M = map(int, input().split())
nums = list(i for i in range(1, N+1))
used = [0] * N
P = [0] * M
dfs(0)
