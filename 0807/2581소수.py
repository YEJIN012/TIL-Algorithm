# 시간초과 + a=1, b=2 고려 못한 경우.
# a = int(input())
# b = int(input())
# N = a

# prime_numbers = []
# while N <= b :

#     s = 2 
#     while N % s != 0 :
#             if s == N-1 :
#                 prime_numbers.append(N)
#                 N += 1
#                 break
#             else :
#                 s += 1
#     else :
#         N += 1

# if len(prime_numbers) == 0 :
#     print(-1)
# else :
#     print(sum(prime_numbers))
#     print(min(prime_numbers))

a = int(input())
b = int(input())
prime_numbers = []

for N in range(a,b+1) :
    if N == 1 :
        pass
    elif N == 2 :
        prime_numbers.append(2)
        # 아래부터는 range 2부터 시작하는 소수 판별 반복문이기 때문에 N이 2일 때 2를 소수로 포함하는 조건이 추가로 필요함.
         
    else :
        for s in range(2,N) : 
            if N % s == 0 :
                break
            elif s == N-1 :
                prime_numbers.append(N)


if len(prime_numbers) == 0 :
    print(-1)
else :
    print(sum(prime_numbers))
    print(min(prime_numbers))