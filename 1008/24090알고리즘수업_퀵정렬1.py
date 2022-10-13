import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
# ! 수업 진행 코드 ! #
def partition2(l, r) :
    global cnt2
    pivot = A[l]
    i, j = l, r
    while i <= j :
        while i <= j and A[i] <= pivot :
            i += 1
        while i <= j and A[j] >= pivot :
            j -= 1
        if  i < j :
            A[i], A[j] = A[j], A[i]
            # ans2 = [A[i], A[j]]
            # print(*sorted(ans2))
            cnt2 += 1
    else :
        A[l], A[j] = A[j], A[l]
        # ans2 = [A[j], A[l]]
        # print(*sorted(ans2))
        cnt2 += 1
        return j

def qsort2(l, r) :
    if  l < r :
        p = partition2(l, r)
        qsort2(l,p-1)
        qsort2(p+1,r)



def partition(l, r) :
    global cnt
    pivot = A[r]
    i = l-1
    for j in range(l, r) :
        if A[j] <= pivot :
            i += 1
            A[i], A[j] = A[j], A[i]
            cnt += 1
            if cnt == K :
                if A[i] <= A[j] :
                    print(A[i], A[j])
                else :
                    print(A[j], A[i])
    if i+1 != r :
        A[i+1], A[r] = A[r], A[i+1]
        cnt += 1
        if cnt == K :
            if A[i + 1] <= A[r] :
                print(A[i+1], A[r])
            else :
                print(A[r], A[i+1])
    return i+1

def qsort(l, r) :
    if  l < r :
        p = partition(l, r)
        qsort(l, p-1)
        qsort(p+1, r)



N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
# cnt2 = 0
qsort(0, N-1)
# qsort2(0, N-1)
if cnt < K :
    print(-1)
# print(cnt)
# print(cnt2)
