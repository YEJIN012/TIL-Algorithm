import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0,start))
    cost[start] = 0
    while q :
        d, v = heapq.heappop(q)
        if d <= cost[v] :           # q에 담긴 비용이 cost에 저장되어있는 비용보다 작거나 같을때만 확인 하면 됨.
            for i in graph[v] :
                new_d = i[1] + d
                if cost[i[0]] > new_d :
                    cost[i[0]] = new_d
                    heapq.heappush(q, (new_d, i[0]))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
cost = [INF] * (N+1)
for _ in range(M) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
dijkstra(start)
print(cost[end])