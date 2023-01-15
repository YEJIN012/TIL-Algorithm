import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s) :
    q = []
    heapq.heappush(q, (0,s))
    distance[s][0] = 0
    while q :
        d, v = heapq.heappop(q)
        for i in graph[v] :
            new_d = d + i[1]
            if new_d < distance[i[0]][k-1] :    # 현재 distance[i[0]]에 담긴 k번째 누적가중치보다 새로운 누적가중치가 작으면,
                distance[i[0]][k-1] = new_d     # 교체.
                distance[i[0]].sort()           # k개의 누적가중치 재정렬.
                heapq.heappush(q, (new_d, i[0]))    # 우선순위큐 push


n, m, k = map(int, input().split())     # n: 도시 개수, m: 간선 개수, k: k번째 최단경로를 구해야함.
graph = [[] for _ in range(n+1)]

# k번째 수를 구하려면 k 이하의 모든 누적가중치를 알아야 하므로,
# 최단경로 배열을 각 도시마다 최단경로를 k개씩 받는 이차원배열로 설정. -> k * (n+1)
distance = [[INF] * k for _ in range(n+1)]

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(1)                 # 1번 도시는 시작도시이다.
for i in range(1, n+1) :
    if distance[i][-1] == INF :
        print(-1)
    else :
        print(distance[i][-1])  # i 도시까지의 k번째 최단경로(index: k-1) 출력.