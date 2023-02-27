# 이항계수 = 조합
def fac(n) :
    ans = 1
    for i in range(1, n+1) :
        ans *= i
    return ans

N, K = map(int, input().split())
print(fac(N) // fac(N-K) // fac(K))