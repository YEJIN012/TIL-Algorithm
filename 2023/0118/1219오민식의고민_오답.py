import sys
input = sys.stdin.readline
INF = int(-1e9)

# 오민식이 도착 도시에 도착했을 때 돈을 무한히 많이 가지고 있을 수 있는지 없는지
# 벨만포드로 음의 사이클 확인!
def bell(n) :
    global B
    money[n] = earn[n]
    for i in range(N) :
        for j in range(N) :
            for b, c in graph[j] :
                if money[j] != INF:
                    if money[j] == 'cc' :       # 현재 노드가 사이클이면 당연히 다음 노드도 사이클
                        money[b] = 'cc'         # 사이클에 포함되는 모든 노드를 cc로 기록.
                    else :
                        new_m = money[j] + earn[b] - c
                        if new_m > money[b] :
                            money[b] = new_m
                            if i == N-1 :       # 사이클 발견시(N번째에도 갱신되는 경우),
                                money[b] = 'cc' # cc로 표시.

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

B = ''
bell(start)
if money[end] == INF :          # 도착지까지 갈 수 없으면,
    ans = 'gg'                  # gg

else :                          # 있으면 -> 사이클 확인.
    if B != -1 :                # 사이클 없으면,
        ans = money[end]            # 벨만으로 인해 기록된 각 도시별 최대 액수 중 도착 도시 금액 출력.
    else :                      # 사이클 있으면,
        if money[end] == 'cc':      # 도착지가 사이클 내부에 있는지 확인.
            ans = 'Gee'                 # 사이클 내부에 있으면, Gee.
        else :                      # 사이클 외부에 있으면,
            ans = money[end]            # 벨만으로 인해 기록된 각 도시별 최대 액수 중 도착 도시 금액 출력.
print(money)
print(ans)


# 5 0 4 6
# 0 1 10000
# 1 2 0
# 2 1 0
# 1 3 0
# 0 3 0
# 3 4 0
# 0 0 1 0 0

# 출력
# [0, 'cc', 'cc', 0, 0]
# 0

# 답
# Gee
