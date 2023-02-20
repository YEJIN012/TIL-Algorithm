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