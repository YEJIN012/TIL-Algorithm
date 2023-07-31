N = int(input())
line = [int(input()) for _ in range(N)]

# 최장 증가 수열 LIS (dp)
dp = [1] * N    # dp[i] : dp[i]를 포함한 이전 수들의 증가 수열길이
for i in range(1, N) :
    for j in range(i) :
        if line[i] > line[j] :
            dp[i] = max(dp[i], dp[j]+1) # 이미 구한 dp[j]의 증가수열길이의 + 1(현재i) 과 현재 dp[i] 중 큰 값

print(N-max(dp))