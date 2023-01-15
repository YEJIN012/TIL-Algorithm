# distance를 이중배열로 최단거리로 갱신 하지않고 진입간선에 의해 나오는 모든 거리를 모두 push
# 출력시 len(distance[i]) >= k 이면, distance[i[k-1]] 출력

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s) :
    q = []
    heapq.heappush(q, [0,s,[1]])
    distance[s].append(0)
    while q :
        d, v, path = heapq.heappop(q)   # 사이클에 의한 무한 loop를 막기위한, path 기록.
        for i in graph[v] :
            if i[0] not in path :       # 방문하지 않았던 노드이면, 계속.
                new_d = d + i[1]
                new_p = path+[i[0]]     # path에 i[0] 경로를 추가한 리스트.
                if new_d not in distance[i[0]] :
                    distance[i[0]].append(new_d)
                    heapq.heappush(q, (new_d, i[0], new_p))
                    dd = distance


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(1)
for i in distance[1:] :
    if len(i) >= k :
        heapq.heapify(i)
        print(i[k-1])
    else :
        print(-1)