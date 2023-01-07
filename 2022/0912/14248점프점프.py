def dfs(s, n) :
    global cnt
    if visited[s] == 0 :
        visited[s] = 1
        cnt += 1            # 함수가 호출 될 때마다, 방문 가능한 돌 +1
        s_1 = s-stone[s]    # 왼쪽으로 점프가능한 위치
        s_2 = s+stone[s]    # 오른쪽으로 점프가능한 위치
        if 0<s_1<=n :       # 점프 위치가 돌다리 범위 내이면,
            dfs(s_1,n)      # 재귀.
        if 0<s_2<=n :
            dfs(s_2,n)
    return


n = int(input())
stone = [0] + list(map(int, input().split()))
s = int(input())
visited = [0] * (n+1)
cnt = 0                     # 방문 가능한 돌들의 개수
dfs(s,n)
print(cnt)