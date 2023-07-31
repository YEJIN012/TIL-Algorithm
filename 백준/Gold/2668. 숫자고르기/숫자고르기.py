N = int(input())
arr = [0] + [int(input()) for _ in range(N)]


# dfs
def dfs(i, s) : # (현재 위치, 출발 위치)
    next = arr[i]
    if next == s :              # 출발 위치로 돌아보면, 중단
        chose.append(next)      # 뽑을 수 있는 숫자
        return
    elif visited[next] == 0 :
        visited[next] = 1
        dfs(next, s)
        visited[next] = 0

chose = []
for i, num in enumerate(arr) :  # 각 출발 숫자를 기준으로 dfs 모두 진행.
    visited = [0] * (N+1)
    visited[i] = 1
    dfs(i, i)   # (현재 위치, 출발 위치)

print(len(chose)-1)
chose.sort()
for n in chose[1:] :
    print(n)