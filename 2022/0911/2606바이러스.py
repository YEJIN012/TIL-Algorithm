def dfs(N, x) :
    global cnt
    virus[x] = 1        # 현재 컴퓨터 표시
    for i in arr[x] :
        if virus[i] == 0 :  # 방문하지 않은 컴퓨터가 있으면,
            cnt += 1        # 바이러스에 걸리게 되는 컴퓨터의 수 +=1
            x = i           # 그 컴퓨터로 이동.
            dfs(N,x)        # 재귀 함수.
    return cnt



N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b  = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
virus = [0] * (N+1)
cnt = 0                 # 바이러스에 걸리게 되는 컴퓨터의 수
print(dfs(N,1))