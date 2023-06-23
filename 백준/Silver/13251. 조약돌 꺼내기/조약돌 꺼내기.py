import math
M = int(input())
color = list(map(int, input().split()))
K = int(input())

com = math.comb
a = 0
for n in color :
    a += com(n,K)

ans = a / com(sum(color), K)
print(ans)