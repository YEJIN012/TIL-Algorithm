def ncr(r, s) :
    if r == 0 :
        print(*lotto)
    else :
        for i in range(s, k-r+1) :
            lotto[6-r] = S[i]
            ncr(r-1, i+1)


inp = list(map(int, input().split()))
k = inp[0]
S = inp[1:k+1]
lotto = [0] * 6
ncr(6, 0)
while True :
    inp = list(map(int, input().split()))
    k = inp[0]
    S = inp[1:k+1]
    if k == 0 :
        break
    else :
        print()
        lotto = [0] * 6
        ncr(6, 0)
