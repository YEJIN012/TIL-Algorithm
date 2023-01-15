import sys
from collections import deque
input = sys.stdin.readline

def topo(k) :
    q = deque(k)
    while q :
        k = q.popleft()
        print(k, end=' ')
        for i in graph[k] :         # 경로를 가지는 노드를 후보로
            indegree[i] -= 1        # 해당 노드의 간선을 하나 지움.(방문)
            if indegree[i] == 0 :   # 간선이 0이 되면,
                q.append(i)         # q에 push


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]    # 인집리스트
indegree = [0] * (N+1)              # 노드별 진입차수 리스트
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

start = []      # 최초 진입차수가 0인 노드
for i in range(1, N+1) :
    if indegree[i] == 0 :
        start.append(i)
topo(start)     # 정렬 함수