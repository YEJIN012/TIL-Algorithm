import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def merge(A, p, q, r) :
    global cnt
    i, j, t = p, q+1, 1
    while i <= q and j <= r :
        if A[i] <= A[j] :
            tmp[t] = A[i]
            t += 1
            i += 1
            cnt +=1 
        else :
            tmp[t] = A[j]
            t += 1
            j += 1
            cnt +=1
    while i <= q :
        tmp[t] = A[i]
        t += 1
        i += 1
        cnt +=1
    while j <= r :
        tmp[t] = A[j]
        t += 1
        j += 1
        cnt +=1

    i, t = p, 1
    while i <= r :
        A[i] = tmp[t]
        i += 1
        t += 1



def merge_sort(A, p, r) :

    if p < r :
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A,q+1, r)
        print('1')
        merge(A, p, q, r)


N, K = map(int,input().split())
A = list(map(int, input().split()))
tmp = [0] * N
cnt = 0
merge_sort(A, 0, N-1)
print(tmp)
print(A)
if cnt < K :
    print(-1)

print('왜안돼')