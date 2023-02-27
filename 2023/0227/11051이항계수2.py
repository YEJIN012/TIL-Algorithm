# 메모리초과
# from itertools import combinations
# # 원래 combinations 모듈은 전체 조합의 리스트를 뽑음.
# # list(combinations(인자들의 list, r))  # list 형태로 출력 필수.
# # 조합의 수를 뽑을 때는 len 사용.
#
# N, K = map(int, input().split())
# N_list = [0] * N    # 리스트를 뽑는게 아니므로 리스트 크기만 맞춰줌.
# k = len(list(combinations(N_list, K)))
# print(k % 10007)

N, K = map(int, input().split())
ans = 1
for i in range(N-K+1, N+1) :
    ans *= i
for i in range(1, K+1) :
    ans //= i
print(ans % 10007)