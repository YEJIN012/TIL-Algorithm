### 벨만포드
# 시작 정점에서부터 각 모든 정점까지의 최단거리 구하는 법.
# 단, 다익스트라와 다르게 사용되는 이유는 가중치로 음수가 존재할 때 사용된다.
# 그래프에 사이클이 존재하면, 최단거리를 무한히 갱신하여 무한대 음수가 나올 수 있기 때문.
# 그래서 벨만포드는,
# heapq없이 정점의 갯수 번 만큼 전체 간선을 모두 조회하여 각 정점의 최단거리를 갱신한다.
# 정점의 갯수 번째에도 최단거리가 갱신되면, 사이클이 존재한다는 것을 알 수 있다.

import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start) :
    value[start] = 0
    for i in range(N) :     # 정점의 수 만큼 반복해서
        for j in range(1, N+1) : # 전체 간선을 모두 조회.    # j: 현재노드
            for b, c in graph[j] :  # b: 현재노드의 인접노드, c: 간선 가중치
                if value[j] != INF and value[b] > value[j] + c :    # 현재노드가 INF가 아니면서 인접노드까지의 가중치합이 인접노드의 현재 최단거리보다 더 작을 때, 갱신.
                    # 현재노드 최단거리가 INF이면 한번도 진입하지 않았다는 것이므로 출발 불가.
                    value[b] = value[j] + c
                    if i == N-1 : # N번째에도 (i == N-1) 값이 갱신되면, 음수 싸이클.
                        # 일반적으로 싸이클이 없는 그래프에서는 마지막노드에서 값이 갱신되지 않음.
                        return -1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
value = [INF] * (N+1)
for _ in range(M) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# start = 1번도시
ans = bellman_ford(1)

if ans == -1 :     # 무한사이클이면,
    print(-1)
else :
    for i in range(2, N+1) :        # 2번 도시부터 가장 빠른 도착시간 출력.
        if value[i] == INF :
            print(-1)
        else :
            print(value[i])
