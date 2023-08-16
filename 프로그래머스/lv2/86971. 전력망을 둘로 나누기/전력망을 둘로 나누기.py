def solution(n, wires):
    answer = n
    node = [[] for _ in range(n+1)]

    for idx, wire in enumerate(wires) :
        a, b = wires[idx]
        node[a].append(b)
        node[b].append(a)

    for idx, wire in enumerate(wires) :
        a, b = wires[idx]
        node[a].pop(node[a].index(b))   # 전선 절단
        node[b].pop(node[b].index(a))
        visited = [0,1] + [0] * (n-1)
        q = [1]
        cnt = 1
        while q :
            si = q.pop(0)
            for ni in node[si] :
                if 0<=ni<=n and visited[ni] == 0 :
                    visited[ni] = 1
                    q.append(ni)
                    cnt += 1
        answer = min(answer, abs(cnt-(n-cnt)))
        node[a].append(b)
        node[b].append(a)
        
    return answer