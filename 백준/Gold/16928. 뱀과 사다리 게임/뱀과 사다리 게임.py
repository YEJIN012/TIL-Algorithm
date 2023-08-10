N, M = map(int,input().split())
arr = [0] * 101
for _ in range(N+M) :
    x, y = map(int,input().split())
    arr[x] = y

def bfs(n) :
    q = [n]
    visited = [0] * 101
    while q :
        i = q.pop(0)

        for di in [i for i in range(1, 7)] :
            ni = i + di
            if 1<=ni<=100 and visited[ni] == 0 :
                if arr[ni] == 0 :   # 뱀과 사다리가 없으면,
                    visited[ni] = visited[i] + 1  # 방문 표시 = 주사위 굴린 횟수 로 생각하고 1씩 증가해가며 표시.
                    q.append(ni)                  # ni만 q에 담기
                else :              # 있으면,  # 무조건 이동하므로, ni에서 다시 시작할 수 없다. 따라서 ni는 방문표시와 q를 담지 않는다.
                    if visited[arr[ni]] == 0 :
                        visited[arr[ni]] = visited[i] + 1
                        q.append(arr[ni])                   # 뱀 사다리 이동 위치만 q에 담기.

            if ni == 100 :
                return visited[ni]

print(bfs(1))
