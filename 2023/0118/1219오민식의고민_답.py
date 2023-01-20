import sys
input = sys.stdin.readline
INF = int(-1e9)

# 사이클이 존재를 찾았을 때,
# 해당 사이클 지점에서 도착지점으로 갈 수 있는지 dfs탐색.
# 갈 수 있으면, 도착지점도 무한히 돈이 갱신되므로, Gee
def dfs(n) :
    global D
    if n == end :
        D = -1
        return    # Gee
    else :
        for b, c in graph[n] :
            if visited[b] == 0 :
                visited[b] = 1
                dfs(b)


# 오민식이 도착 도시에 도착했을 때 돈을 무한히 많이 가지고 있을 수 있는지 없는지
# 벨만포드로 음의 사이클 확인!
def bell(n) :
    global B
    money[n] = earn[n]
    for i in range(N) :
        for j in range(N) :
            for b, c in graph[j] :
                new_m = money[j] + earn[b] - c
                if money[j] != INF and new_m > money[b] :
                        money[b] = new_m
                        if i == N-1 :       # 사이클 발견시(N번째에도 갱신되는 경우),
                            dfs(j)
                            if D == -1 :   # 사이클에 도착지점도 영향을 받는지 확인.
                                B = -1
                                return



N, start, end, M = map(int, input().split())
graph = [[] for _ in range(N)]
money = [INF] * N
for _ in range(M) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
earn = list(map(int, input().split()))
visited = [0] * N

D = ''
B = ''
bell(start)
if B == -1:               # 사이클에 영향을 받는다
    ans = 'Gee'             # -> Gee
elif money[end] == INF :    # 아예 도착을 못한다
    ans = 'gg'              # -> gg
else :                      # 도착가능
    ans = money[end]        # -> 벨만으로 인해 기록된 각 도시별 최대 액수 중 도착 도시 금액 출력.

print(ans)