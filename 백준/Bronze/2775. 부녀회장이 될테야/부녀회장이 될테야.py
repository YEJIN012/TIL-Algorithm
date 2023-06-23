tc = int(input())
for _ in range(tc) :
    k = int(input())    # 층
    n = int(input())    # 호
    # 2층 3호
    # 1 2 3
    # 1 (1+2) (1+2+3)
    # 1 1+(1+2) 1+(1+2)+(1+2+3)
    # 1 1+(1+1+2) 1+(1+1+2)+(1+1+2+1+2+3)
    ppl = []
    for i in range(1, n+1) :
        ppl.append(i)

    for _ in range(k) :
        for i in range(1, n) :
            ppl[i] += ppl[i-1]
    print(ppl[-1])