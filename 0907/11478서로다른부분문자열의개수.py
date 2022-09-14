import sys

N = sys.stdin.readline()[:-1]
set_N = []
for k in range(1,len(N)+1) :
    for i in range(len(N)+1) :
        if i+k < len(N)+1 :
            K = N[i:i+k]
            set_N.append(K)
print(len(list(set(set_N))))
# print(len(set(set_N))) 도 가능


# 포기..... 버리자 #
# N = list(N) + ['']*(len(N)-1)
# set_N = []
# for i in range(len(N)) :
#     for j in range(len(N)) :
#         if j != i :
#             for l in range(len(N)) :
#                 if l != i and l != j :
#                     K = N[i] + N[j] + N[l]
#                     set_N.append(K)
# print(list(set(set_N)))
# print(len(list(set(set_N))))
