# DP
N = int(input())
A = list(map(int,input().split()))
answer = [-1] * N
for i in range(N-2,-1,-1) : # 뒤에 있는 수들을 비교하므로 역순으로 진행.
    for j in range(i+1, N) :
        if A[i] < A[j] :
            answer[i] = A[j]
            break
        else :
            if A[i] < answer[j] :
                answer[i] = answer[j]
                break
            elif answer[j] == -1 :
                break
print(*answer)