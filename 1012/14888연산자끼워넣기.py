def f(i, ans) :
    global minV
    global maxV

    if i == N :             # N개의 수와 N-1개의 연산자를 다 사용하고 나면,
        if maxV < ans :     # 최대값, 최소값 갱신
            maxV = ans
        if minV > ans :
            minV = ans
    else :
        for j in range(N-1) :
            if used[j] == 0 :
                used[j] = 1
                if operator[j] == 0 :
                    f(i+1, ans+nums[i])
                elif operator[j] == 1 :
                    f(i+1, ans-nums[i])
                elif operator[j] == 2 :
                    f(i+1, ans*nums[i])
                elif operator[j] == 3 :
                    if ans < 0 :
                        f(i+1, -(-ans//nums[i]))
                    else :
                        f(i+1, ans//nums[i])
                used[j] = 0

N = int(input())
nums = list(map(int,input().split()))
operator_ = list(map(int,input().split()))
maxV = -1000000000
minV = 1000000000
operator = []               # 연산자 고유번호를 원소로 받는 연산자 리스트 제작.
for i in range(4) :
    while operator_[i] :
        operator.append(i)
        operator_[i] -= 1
used = [0]*(N-1)            # 연산자 사용체크 리스트.
f(1, nums[0])

print(maxV)
print(minV)