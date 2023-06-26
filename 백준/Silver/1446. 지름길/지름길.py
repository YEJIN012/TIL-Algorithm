N, D = map(int, input().split())
road = [list(map(int,input().split())) for _ in range(N)]
dp = [i for i in range(D+1)]

for i in range(D+1) :
    dp[i] = min(dp[i], dp[i-1]+1)    # 이전에 끊긴 지름길이 있을 경우를 고려하여 최소값을 이어받는다.
    for S, E, l in road :
        if E <= D and l < E-S and S == i :  # 시작위치를 기준으로 
            dp[E] = min(dp[E], dp[S]+l)     # 도착위치에 최단거리 갱신
print(dp[D])