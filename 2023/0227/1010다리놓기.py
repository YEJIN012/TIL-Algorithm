# 조합의 수
T = int(input())
for _ in range(T) :
    r, n = map(int, input().split())    # r: 서쪽 사이트 수, n: 동쪽 사이트 수
    ans = 1
    for i in range(1,n+1) :
        ans *= i
    for i in range(1, n-r+1) :
        ans //= i
    for i in range(1, r+1) :
        ans //= i
    print(ans)