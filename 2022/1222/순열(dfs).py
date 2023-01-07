def npr(i,r) :
    if i == r :
        print(A)
        ans = ''.join(map(str, A))
        total_num.append(int(ans))
    else :
        for j in range(N) :
            if used[j] == 0 :
                A.append(numbers_list[j])
                used[j] = 1
                npr(i+1,r)
                A.pop(-1)
                used[j] = 0



answer = 0
total_num = []
numbers_list = [1,2,3]

N = len(numbers_list)
for r in range(1, N+1) :
    used = [0] * N
    A  = []
    npr(0,r)
print(total_num)