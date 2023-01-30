import sys
import heapq
input = sys.stdin.readline

def prim(start, V) :
    MST = [0] * (V+1)       # MST 담긴 노드 표시.
    q = [(0,start)]
    total = 0               # 최소 가중치 총합.
    cnt = 0
    while cnt < V :     # MST 간선갯수 V-1개 뽑을 때까지 반복(시작점을 제외하고 노드 V-1개)
        d, n = heapq.heappop(q)     # d:가중치 n:노드
        if MST[n] == 0 :
            MST[n] = 1
            total += d
            cnt += 1
            for k, c in edge[n] :
                heapq.heappush(q,(c,k))     #(가중치,노드)
    return total

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
for _ in range(E) :
    a, b, c = map(int,input().split())  # a정점과 b정점이 가중치 c간선으로 연결.
    edge[a].append((b,c))
    edge[b].append((a,c))
print(prim(1,V))

# 프림 알고리즘
# def prim(graph, start_node):
#     visited[start_node] = 1 # 방문 갱신
#     candidate = graph[start_node] # 인접 간선 추출
#     heapq.heapify(candidate) # 우선순위 큐 생성
#     mst = [] # mst
#     total_weight = 0 # 전체 가중치
#
#     while candidate:
#         weight, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
#         if visited[v] == 0: # 방문하지 않았다면
#             visited[v] = 1 # 방문 갱신
#             mst.append((u,v)) # mst 삽입
#             total_weight += weight # 전체 가중치 갱신
#
#             for edge in graph[v]: # 다음 인접 간선 탐색
#                 if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (순환 방지)
#                     heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입