def bfs(i) :
    q = [i]
    visited[i] = 1
    find = 0
    while q:
        i = q.pop(0)
        for k in [i-1, i+1, 2*i] :
            if 0<=k<100001 and visited[k] == 0 :    # N,M이 최대 100000까지 들어올 수 있으므로, index는 100000까지 가능!
                if k == K :             # 동생이 있는 곳에 도달하면,
                    find = 1            # 찾았다!
                    print(visited[i])   # 이동시간 출력
                    break
                else :
                    visited[k] = visited[i]+1   # 이동시간을 1초씩 들려가면서 visited에 기록.
                    q.append(k)
        if find == 1 :
            break

N, K = map(int, input().split())
visited = [0] * 100001              # N,M이 최대 100000까지 들어올 수 있으므로, 100001개 만들기.
cnt = 0
if N == K :                         # 같은 위치에 있을 때 따로.....빼구...
    print(0)
else :
    bfs(N)