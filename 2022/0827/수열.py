### 시간초과 ###
# N, K = map(int, input().split())
# temper = list(map(int, input().split()))
# max = sum(temper[:K])
# for i in range(N-K+1) :
#     total = sum(temper[i:i+K])
#     if max < total :
#         max = total
# print(max)

N, K = map(int, input().split())
temper = list(map(int, input().split()))
max = sum(temper[0:K])
sum = sum(temper[0:K])
for i in range(1, N-K+1) :
    sum = sum - temper[i-1] + temper[i+K-1]
    if max < sum :
        max = sum
print(max)
