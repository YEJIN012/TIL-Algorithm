# distance를 이중배열로 최단거리로 갱신 하지않고 진입간선에 의해 나오는 모든 거리를 모두 push
# 출력시 len(distance[i]) >= k 이면, distance[i[k-1]] 출력

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s) :
    q = []
    path1 = [0]*(n+1)                       # path: 각 노드의 방문 여부 표시.
    path1[s] = 1
    heapq.heappush(q, [0,s,path1])
    distance[s].append(0)
    while q :
        d, v, path = heapq.heappop(q)       # 사이클에 의한 무한 loop를 막기위한, path 기록.
        for i in graph[v] :
            if path[i[0]] :                 # 방문했던 노드이면,
                continue                    # 무시.
            new_d = d + i[1]
            new_path = list(path)
            new_path[i[0]] = 1              # i[0] 방문을 표시한 path 리스트.
            distance[i[0]].append(new_d)
            # print(distance)
            distance[i[0]]=list(set(distance[i[0]]))
            heapq.heappush(q, (new_d, i[0], new_path))


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[] for _ in range(n+1)]     # 노드까지 나올 수 있는 모든 경로의 거리를 저장하는 리스트.
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(1)
for i in distance[1:] :
    if len(i) >= k :
        i.sort()        # 모든 경로의 거리를 정렬
        print(i[k-1])           # k번째 출력.
    else :
        print(-1)


