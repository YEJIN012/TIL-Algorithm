# 물건을 담을 때와 담지않았을 때의 가치를 이중배열에 기록함
N, K = map(int, input().split())
arr = [[0] * (K+1) for _ in range(N+1)] # i : 물건갯수, j : 배낭 무게
for i in range(1, N+1) :
    W, V = map(int, input().split())
    for j in range(1, K+1) :
        if W <= j : # 현재 물건을 담을 수 있을 때,
            arr[i][j] = max(arr[i-1][j-W] + V, arr[i-1][j]) # [i-1개의 물건갯수][j-현재물건의 무게] + 현재물건의 가치(=현재물건을 담고 동일갯수, 동일무게가 되었을 때의 가치)와
                                                            # [i-1개의 물건갯수][j](=현재물건을 담지 않고 현재의 동일갯수,동일무게 되었을 때의 가치) 를 비교하여 동일 상황에서의 최대가치 갱신
        else :
            arr[i][j] = arr[i - 1][j]
print(arr[N][K])