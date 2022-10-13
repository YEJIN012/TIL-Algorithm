def f(i) :
    if i == M :
        print(*A)
    else :
        for j in range(N) :
            if used[i][j] == 0 :
                # 비내림차순 순열을 만들기 위한 조건
                # -> A[0]는 비내림차순 확인 필요없고 A[1]이상은 앞자리 수보다 크거나 같은 값만 가능.
                if (i > 0 and A[i-1] <= nums[j]) or i == 0 :
                    A[i] = nums[j]
                    used[i][j] = 1
                    f(i + 1)
                    used[i][j] = 0


N, M = map(int, input().split())
nums = list(i for i in range(1, N+1))
A = [0] * M
# 각자리마다 중복가능하므로 [0]*N을 M개의 행만큼 만들어줌.
used = [[0] * N for _ in range(M)]
f(0)