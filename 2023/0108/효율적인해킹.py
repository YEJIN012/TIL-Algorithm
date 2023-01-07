import sys
from collections import deque       ## deque 필수;;;
input = sys.stdin.readline

def bfs(n) :
    check = [0] * (N + 1)
    q = deque([n])
    check[i] = 1
    cnt = 0
    while q :
        k = q.popleft()
        for d in graph[k] :
            if check[d] == 0 :
                q.append(d)
                check[d] = 1
                cnt += 1
    return cnt

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    graph[b].append(a)

MaxV = 0
comp = ''
for i in range(1, N+1) :
    cnt = bfs(i)
    if MaxV < cnt :
        MaxV = cnt
        comp = str(i) + ' '
    elif MaxV == cnt :
        comp += str(i) + ' '
print(comp[:-1])

# 6 5
# 1 2
# 2 3
# 3 1
# 4 5
# 5 6

# 1 2 3 6
