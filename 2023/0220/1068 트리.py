INF = int(1e9)

N = int(input())
child = [0] * N     # 자식노드가 있는 노드에 count 1
par_tree = list(map(int,input().split()))   # 각 노드(index)의 부모가 저장된 list
d = int(input())                # 지울 노드의 번호
leaf = -1
q = []      # 삭제된 노드의 자식노드

if par_tree[d] == -1 :              # 1. 루트 노드를 제거 할 경우,
    leaf = 0
    print(leaf)

else :                              # 2. 그 외에 경우,
    par_tree[d] = -INF              # 제거 노드를 지우고 시작.
    for i in range(N):
        if par_tree[i] == d:        # 삭제된 노드를 부모로 가진 노드
            par_tree[i] = -INF      # 해당 노드를 지우고
            q.append(i)             # 그 노드의 하위 노드를 탐색하기 위해, queue push

    while q:                        # 삭제된 노드 하위 노드에서 반복.
        k = q.pop()
        for i in range(N):
            if par_tree[i] == k:
                par_tree[i] = -INF
                q.append(i)

    for i in range(N) :                 # 해당 노드를
        for j in range(N) :
            if par_tree[j] == i :       # 부모노드로 저장한 노드가 있으면,
                child[i] = 1            # 자식이 있는 노드로 판별.
                break
        if par_tree[i] == -INF :        # 삭제된 노드도
            child[i] = 1                # 1로 표시 (결과값 leaf 노드를 빠르게 찾기 위해.)

    print(N-sum(child))                 # 전체 노드 중, 자식노드가 없고 삭제되지 않은 노드 count