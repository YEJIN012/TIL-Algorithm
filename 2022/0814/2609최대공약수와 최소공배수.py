N, M = map(int, input().split())

### 시간초과 방법 ###
# for i in range(1,M+1) :
#     for j in range(1,N+1) :
#         if N * i == M * j :
#             print((N * M) // (N * i))
#             print(N * i)
#             break
#     if N * i == M * j :
#         break


N_list = [] # 자연수 N의 약수 리스트
ans1 = 0
for i in range(N, 0, -1) : # 자연수 N부터 1까지 나누어 떨어지는 약수 구하기(내림차순).
    if N % i == 0 :
        N_list.append(i)

for i in N_list : # N의 약수들 중 M의 약수도 되는 것 찾기.
    if M % i == 0 :
        ans1 = i
        break

ans2 = N * M // ans1 # 두 자연수의 합 = 최대공약수 * 최소공배수

print(ans1)
print(ans2)



