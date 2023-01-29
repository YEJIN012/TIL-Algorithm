import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd() :
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

n = int(input())
m = int(input())
cost = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n + 1):
    cost[i][i] = 0
for _ in range(m) :
    a, b, c = map(int, input().split())
    if cost[a][b] > c :
        cost[a][b] = c

floyd()

for i in range(1,n+1) :
    for j in range(1, n+1) :
        ans = 0 if cost[i][j] == INF else cost[i][j] # i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
        print(ans, end=' ')
    print()