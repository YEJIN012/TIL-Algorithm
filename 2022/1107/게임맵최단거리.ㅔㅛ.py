def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visited = list([0] * M for _ in range(N))
    print(visited)
    q = [(0, 0)]
    visited[0][0] = 1
    while q:
        i, j = q.pop(0)
        if i == N-1 and j == M-1 :
            answer = visited[i][j]
            break
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and visited[ni][nj] == 0 :
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))

    if answer == 0 :
        answer = -1


    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
