import sys
input = sys.stdin.readline

N = int(input())
graph  = [[] for _ in range(N+1)]
par = [0] * (N+1)       # 자식노드를 index로 부모번호를 저장
par_cnt = 0             # 구해진 부모노드의 갯수
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 시간 초과 #
# while par_cnt < N-1 :
#     for i in range(2,N+1) :
#         if len(graph[i]) == 1 :     # 간선이 하나 밖에 없는 노드는 leaf
#             par[i] = graph[i][0]    # leaf노드의 부모로 저장.
#             par_cnt += 1            # 구한 부모노드 +1
#             graph[i].pop()          # 노드 삭제.
#     for i in range(2,N+1) :
#         k = 0
#         while len(graph[i]) > 1 and k < len(graph[i]) :     # 간선이 2개 이상이면, 삭제가능한(이미 부모노드가 구해진) 간선찾기
#             if par[graph[i][k]] :       # 이미 부모노드가 구해진 노드가 간선
#                 graph[i].pop(k)         # 삭제
#             else :
#                 k += 1

# bfs
q = [1]                             # 루트부터 너비우선탐색 시작.
while q :
    i = q.pop(0)
    for w in graph[i] :             # 인접된 노드 중
       if not par[w] :              # 아직 부모노드를 찾지 못한 node가 있으면,(이미 부모노드가 들어가있는 노드는 내자식노드임.)
            par[w] = i              # 그 노드가 내 자식노드.
            if w != 1 :             # 루트 1을 제외하고 deque
                q.append(w)

for i in range(2, N+1) :
    print(par[i])
