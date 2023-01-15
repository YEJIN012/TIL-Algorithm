import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)      # 무한의 의미로 10억 설정

def dijkstra(start) :
    q = []
    # 다익스트라에서의 힙 우선순위 = 거리
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q :
        d, v = heapq.heappop(q)     # d : 해당 노드까지 걸린 최소 누적거리, v : 가장 거리가 짧은 노드(현재 노드)
        if distance[v] < d :        # 이미 q에 담겨 처리된 적이 있는 노드라면(최소거리가 아니라면),
            continue                # 무시.
        for i in graph[v] :         # 인접 노드 순회
            new_d = d + i[1]        # d : 현재 노드까지 최단거리 + 인접노드까지의 거리     # i[1] = c
            if distance[i[0]] > new_d :     # 인접노드까지의 최단 거리 갱신
                distance[i[0]] = new_d
                heapq.heappush(q, (new_d, i[0]))    # 갱신시, (거리,노드)push

V, E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)
for i in range(1, V+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])