# import sys
# sys.setrecursionlimit(10**8)
#
# def dfs(n) :
#     global flight_cnt
#     visited[n] = 1
#     for w in graph[n] :
#         if visited[w] == 0 :
#             flight_cnt += 1
#             dfs(w)
#
#
# for tc in range(1, int(input())+1) :
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M) :
#         a, b = map(int,input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     minV = 10**8
#     for n in range(1, N+1) :
#         flight_cnt = 0
#         visited = [0] * (N+1)
#         dfs(n)
#         # print(flight_cnt)
#         # print(visited)
#         if sum(visited) == N and flight_cnt < minV :
#             minV = flight_cnt
#
#     print(minV)


for tc in range(1, int(input())+1) :
    N, M = map(int, input().split())
    for _ in range(M) :
        a, b = map(int,input().split())
    print(N-1)
