import sys
sys.setrecursionlimit(int(1e5))

N = int(input())
par = [0] * (N+1)       # 각 노드의 부모노드 list
visited = [0] * (N+1)
level = [0] * (N+1)     # 각 노드의 level list
tree = [[] for _ in range(N+1)]

for _ in range(N-1) :
    i, j  = map(int, sys.stdin.readline().split())
    tree[i].append(j)
    tree[j].append(i)

# 문제에서 부모,자식노드 구분이 없이 연결 정보가 주어질 때는 ( <-> 3584번과 비교 )
# 인접리스트에서
# 루트노드부터 시작하는 dfs탐색을 진행하여 level과 부모노드를 저장해둬야 함.

# 레벨 찾기 & 부모 노드 저장
def dfs(n, cnt) :
    visited[n] = 1      # 트리를 거슬러 올라가지 않기 위해, 방문표시 필요.
    level[n] = cnt
    for adj in tree[n] :
        if visited[adj] == 0 :
            par[adj] = n
            dfs(adj, cnt + 1)

# 시작 두 노드의 level 맞추기 & 공통조상 찾기
def find(a, b):
    while level[a] != level[b]:
        if level[a] < level[b]:  # level 조절이 필요한 노드(level이 높은 노드)의 부모노드로 이동.
            b = par[b]
        else:
            a = par[a]
    while a != b:
        a = par[a]
        b = par[b]
    else:
        return a

dfs(1, 0)       # 레벨 및 부모노드 구하기.

M = int(input())
for _ in range(M) :         # M개의 쌍 공통 부모 찾기.
    a, b = map(int, sys.stdin.readline().split())
    print(find(a, b))