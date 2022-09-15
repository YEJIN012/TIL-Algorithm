# !!재귀!! #
# import sys
# sys.setrecursionlimit(100000)
# def dfs(i) :
#     visited[i] = 1
#     for w in graph[i] :
#         if visited[w] == 0 :
#             dfs(w)
#
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M) :
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# visited = [0] * (N+1)
# cnt = 0                             # 연결 요소의 개수
# while sum(visited) < N :            # 주어진 정점 중에 방문하지 못한 정점이 있으면,
#     for i in range(1, N+1) :
#         if visited[i] == 0 :        # 방문하지 못한 정점 찾기.
#             dfs(i)                  # 그 정점부터 깊이우선탐색 시행.
#             # print(visited)
#             cnt += 1                # 한번 돌고 나면 연결요소 +1
#             break
# print(cnt)


# !!stack!! #
def dfs(i) :
    visited[i] = 1
    for w in graph[i] :
        if visited[w] == 0 :
            dfs(w)
    stack = []
    visited[i] = 1
    while True :
        for w in graph[i] :
            if visited[w] == 0 :
                stack.append(i)
                visited[w] = 1
                i = w
                # print(w)
                break
        else :
            if stack :
                i = stack.pop()
            else :
                break


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)
cnt = 0                             # 연결 요소의 개수
while sum(visited) < N :            # 주어진 정점 중에 방문하지 못한 정점이 있으면,
    for i in range(1, N+1) :
        if visited[i] == 0 :        # 방문하지 못한 정점 찾기.
            dfs(i)                  # 그 정점부터 깊이우선탐색 시행.
            # print(visited)
            cnt += 1                # 한번 돌고 나면 연결요소 +1
            break
print(cnt)