paper = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]

def bingo_check(n) :
    bingo_cnt = 0
    for i in range(5) :
        if sum(paper[i]) == -5 :
            bingo_cnt += 1
    for j in range(5) :
        total = 0
        for i in range(5) :
            if paper[i][j] == -1 :
                total += 1
        if total == 5 :
            bingo_cnt += 1

    total1 = 0
    for l in range(5) :
        if paper[l][l] == -1 :
            total1 += 1
    if total1 == 5 :
        bingo_cnt += 1

    total2 = 0
    for m in range(5) :
        if paper[m][4-m] == -1 :
            total2 += 1
    if total2 == 5 :
        bingo_cnt += 1

    return bingo_cnt


def num_check(m, n) :
    for i in range(5):
        for j in range(5):
            if paper[i][j] == call[m][n]:
                paper[i][j] = -1

bingo_cnt = 0
for m in range(5) :
    for n in range(5) :
        num_check(m, n)
        if bingo_check(0) >= 3 :
            print(m * 5 + n + 1)
            break
    if bingo_check(0) >= 3:
        break