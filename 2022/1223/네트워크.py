def solution(n, computers):
    answer = 0              # 네트워크 갯수
    visited = [0] * n       # 각 컴퓨터 방문표시 list

    for p in range(n):      # 컴퓨터 전체 순회
        if visited[p] == 0: # 방문되지 못한 컴퓨터가 있으면 그 컴퓨터부터 bfs 탐색시작.

            # bfs
            q = [p]
            visited[p] = 1
            while q:
                i = q.pop(0)
                candid = [] # i 컴퓨터로부터의 네트워크 연결 후보군
                for j in range(n):
                    if computers[i][j] == 1:    # computers[i][j]가 1이면,
                        candid.append(j)        # j 컴퓨터와 연결되어있다는 것, 후보군에 j push.
                for dj in candid:               # 후보군들 중
                    if visited[dj] == 0:        # 방문되지 못한 컴퓨터가 있으면,
                        visited[dj] = 1         # 방문표시.
                        q.append(dj)            # queue에 해당 컴퓨터 pop
            answer += 1     # bfs 탐색이 끊기면 네트워크 + 1

    return answer