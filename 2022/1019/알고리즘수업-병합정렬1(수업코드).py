import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def msort(i, N) :               # i 병합구간의 시작 인덱스, N 구간의 원소 개수 l = i, r = i+N-1
    global cnt
    if N == 1 :                 # 분할한 원소가 1개만 남은 경우
        return
    else :
        msort(i, N//2)          # i : 병합할 왼쪽 구간의 시작 인덱스.
        msort(i+N//2, N-N//2)     # j : 병합할 오른쪽 구간의 시작 인덱스.

        k = 0
        l, r = i, i+N//2
        while l < i+N//2 and r < i+N :  # i : 왼쪽 구간에서 비교할 위치, j : 오른쪽 구간에서 비교할 위치.
            if L[l] <= L[r] :       # 오름차순, 작은 숫자 먼저 tmp에 복사
                tmp[k] = L[l]
                l += 1              # 왼쪽구간에서 선택된 경우 l++
            else :
                tmp[k] = L[r]
                r += 1              # 오른쪽 구간에서 선택된 경우 r++
            k += 1
            cnt += 1
            # print(tmp)
        if cnt == K :
            print(tmp[k-1])

        while l < i+N//2 :          # 왼쪽구간에 남은 숫자가 있으면 모두 tmp에 복사
            tmp[k] = L[l]
            l += 1
            k += 1
            cnt += 1
            # print(tmp)

        if cnt == K :
            print(tmp[k-1])

        while r < i+N :
            tmp[k] = L[r]
            r += 1
            k += 1
            cnt += 1
            # print(tmp)

        if cnt == K :
            print(tmp[k-1])

        for x in range(N) :         # 병합한 결과 원본에 복사.
            L[i+x] = tmp[x]
        return i
        



N, K = map(int,input().split())
L = list(map(int, input().split()))
tmp = [0] * N
cnt = 0
msort(0, N)

if cnt < K :
    print(-1)