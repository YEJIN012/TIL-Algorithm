t = int(input())
for _ in range(t) :
    N = int(input())
    par = [0] * (N+1)   # 각 노드(index)의 부모노드 저장.
    for _ in range(N-1) :
        i, j  = map(int, input().split())
        par[j] = i

    a, b = map(int, input().split())
    a_par = [a]
    b_par = [b]

    while par[a] :
        a_par.append(par[a])     # a의 조상노드 모두 저장.
        a = par[a]

    while par[b] :
        b_par.append(par[b])     # b의 조상노드 모두 저장.
        b = par[b]

    # a,b 부모 리스트를 역순으로 조회(같은 루트레벨에서 시작하기 위해)
    i = len(a_par)-1
    j = len(b_par)-1
    while a_par[i] == b_par[j] :
        i -= 1
        j -= 1
    print(a_par[i+1])