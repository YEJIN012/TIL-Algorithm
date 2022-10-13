def fac(n) :
    k = 1
    if n == 0 :
        return k
    else :
        for i in range(1,n+1) :
            k *= i
    return k

def ncr(n,r) :
    return fac(n) / (fac(n-r) * fac(r))

N, M, K = map(int, input().split())
# 1.
# 당첨될 경우의 수
# "적어도"이므로 (K만 맞는 경우) + (K+1개 맞는 경우) ... (M개 맞는 경우) 까지 다 구함.
c = 0
while M >= K :
    if N-M < M-K :  # N-M이 M-K보다 작은 경우의 수는 구할 수 없으므로, K값을 계속 키워줘야 함.
        K += 1
    else :
        c += ncr(M,K) * ncr(N-M,M-K)
        K += 1
# 2.
# 모든 경우의 수
p = ncr(N,M)

ans = c / p
print(ans)