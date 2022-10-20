def bfs(i) :
    q = [i]
    visited[i] = 0
    while q:
        i= q.pop(0)
        for k in [i-1, i+1, 2*i] :
            if 0<=k<100000 and visited[k] == 0 :
                if k == K :
                    print(visited[i]+1)
                else :
                    visited[k] = visited[i]+1
                    q.append(k)


N, K = map(int, input().split())
visited = [0] * 100000
cnt = 0
bfs(0)