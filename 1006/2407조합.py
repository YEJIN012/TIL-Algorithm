# import sys
# sys.setrecursionlimit(10**9)
#
# def ncm(i,k) :
#     global cnt
#     if i == M :
#         cnt += 1
#     else :
#         for j in range(k,N-(M-i)+1) :
#             ncm(i+1, j+1)
#
# N, M = map(int, input().split())
# cnt = 0
# n = list(i for i in range(N))
# C = [0] * M
# ncm(0,0)
# print(cnt)
def fac(n) :
    if n == 0 :
        return 1
    else :
        return fac(n-1)*n


N, M = map(int, input().split())
print((fac(N))//(fac(N-M)*fac(M)))