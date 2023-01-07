# 조합 + 다른무게
N, M = map(int, input().split())
ball = list(map(int, input().split()))
cnt = 0
for i in range(N-1) :
    for j in range(i+1, N) :
        if ball[i] != ball[j] :
            cnt += 1

print(cnt)