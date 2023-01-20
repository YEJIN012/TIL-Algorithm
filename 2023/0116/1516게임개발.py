### 위상 정렬 -> queue
# 다익스트라랑 비슷하게 크기 비교해서 갱신하면 되는데
# 그냥 최단거리가 아니라 게임룰이 있어서 더 긴시간으로 갱신.

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree= [0] * (N+1)
my_time = [0] * (N+1)
total_time = [0] * (N+1)
for i in range(1, N+1) :
    building = list(map(int, input().split()))
    total_time[i] += building[0]
    my_time[i] += building[0]
    for j in range(1, len(building)-1) :
            graph[building[j]].append(i)
            indegree[i] += 1

q= deque()
# 진입차수가 0인 시작점 찾기.
for i in range(1, N+1) :
    if indegree[i] == 0 :
        q.append(i)

while q :
    v = q.popleft()
    for i in graph[v] :
        indegree[i] -= 1
        # 1->4 와 1->3->4 의 순서 비교 필요.
        # 시간이 더 오래 걸리는 것이 반드시 지켜야하는 순서라는 의미이다.
        # node 1를 짓고 바로 온 total_time[4] 와 1->3을 짓고 온 new_t 중 큰 값으로 갱신..
        new_t = total_time[v] + my_time[i]
        if total_time[i] < new_t :
            total_time[i] = new_t
        if indegree[i] == 0 :
            q.append(i)


for i in range(1, N+1) :
    print(total_time[i])