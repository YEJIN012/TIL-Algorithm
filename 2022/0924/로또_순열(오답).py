def npr(i) :
    if i == 6 :
        print(' '.join(str(lotto)))
    else :
        for j in range(k) :
            if choosed[S[j]] == 0 :
                lotto[i] = S[j]
                choosed[S[j]] = 1
                npr(i+1)
                choosed[S[j]] = 0


while True :
    inp = list(map(int, input().split()))
    k = inp[0]
    S = inp[1:k+1]
    if k == 0 :
        break
    else :
        choosed= [0] * 50
        lotto = [0] * 6
        npr(0)
