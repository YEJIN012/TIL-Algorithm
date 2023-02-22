def depth(N, tree) :
    dep = [0] * (N+1)
    for i in range(N) :
        q = tree[i]
        while q :


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1) :
    i, j  = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)
M = int(input())

for _ in range(M) :         # M개의 쌍 공통 부모 찾기.
    a, b = map(int, input().split())
