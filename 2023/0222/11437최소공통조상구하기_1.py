N = int(input())
par = [0] * (N+1)   # 각 노드(index)의 부모노드 저장.
for _ in range(N-1) :
    i, j  = map(int, input().split())
    par[j] = i
M = int(input())
a_par = []
b_par = []
for _ in range(M) :         # M개의 쌍 공통 부모 찾기.
    a, b = map(int, input().split())
    t = a                   # a 노드의 조상노드 추적.
    p = 0
    while p != 1 :          # 루트노드가 나올 때까지
        p = par[t]
        a_par.append(p)     # 조상노드 모두 저장.

    t = b                   # b 노드의 조상노드 추적.
    p = 0
    while p != 1 :          # 루트노드가 나올 때까지
        p = par[t]
        b_par.append(p)     # 조상노드 모두 저장.

    i = -1      # a,b 부모 리스트를 역순으로 조회(같은 루트레벨에서 시작하기 위해)
    while a_par[i] != b_par[i] :
        i += 1
    else :
        ans = a_par[i]
    print(a_par[i])