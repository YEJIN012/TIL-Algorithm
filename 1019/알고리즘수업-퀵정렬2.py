# 제출코드
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def partition(l, r) :
    global cnt, K, A
    pivot = A[r]
    i = l-1
    for j in range(l, r) :
        if A[j] <= pivot :
            i += 1
            A[i], A[j] = A[j], A[i]
            cnt += 1
            if cnt == K :               # K 번째 교환에서, A 출력
                for k in A :
                    print(k, end=' ')
                exit()
    if i+1 != r :
        A[i+1], A[r] = A[r], A[i+1]
        cnt += 1
        if cnt == K :
            for k in A:                # K 번째 교환에서, A 출력
                print(k, end=' ')
            exit()
    return i+1

def qsort(l, r) :
    if  l < r :
        p = partition(l, r)
        qsort(l, p-1)
        qsort(p+1, r)



N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
qsort(0, N-1)
if cnt < K :        # 전체 교환 횟수가 K보다 작으면
    print(-1)       # -1 출력.