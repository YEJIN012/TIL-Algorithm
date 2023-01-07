def ncr(p, i) :         # p = 번호pick 갯수
    if p == 6 :
        print(*lotto)
    else :
        for j in range(i, k-(6-p)+1) :  # 번호후보군 : i ~ 6-p개 남겨두고 전부.
            lotto[p] = S[j]             # p 자리에 S[j] 뽑기
            ncr(p+1, j+1)               # p+1 을 뽑으려면, j+1 부터가 후보군.


inp = list(map(int, input().split()))
k = inp[0]
S = inp[1:k+1]
lotto = [0] * 6
ncr(0, 0)
while True :
    inp = list(map(int, input().split()))
    k = inp[0]
    S = inp[1:k+1]
    if k == 0 :
        break
    else :
        print()
        lotto = [0] * 6
        ncr(0, 0)
