paper = [list(map(int,input().split())) for _ in range(3)]
call = [list(map(int,input().split())) for _ in range(3)]

def binggo_check(paper) :
    global binggo_cnt
    visited = [[0]*3 for _ in range(3)]
    for i in range(3) :
        for j in range(3) :
            if paper[i][j] == -1 and visited[i][j] == 0 :
                for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                    k = 1
                    five_cnt = 1
                    while 0 <= i + di * k < 3 and 0 <= j + dj * k < 3:
                        ni, nj = i + di * k, j + dj * k
                        if paper[ni][nj] == -1 and (visited[ni][nj] == 0 or visited[ni][nj] == 1) :
                            visited[ni][nj] = 1
                            five_cnt += 1
                            k += 1
                        else:
                            break
                    else:
                        k = -1
                        while 0 <= i + di * k < 3 and 0 <= j + dj * k < 3:
                            ni, nj = i + di * k, j + dj * k
                            if paper[ni][nj] == -1 and (visited[ni][nj] == 0 or visited[ni][nj] == 1) :
                                visited[ni][nj] = 1
                                five_cnt += 1
                                k -= 1
                            else:
                                break
                        else:
                            if five_cnt == 3:
                                binggo_cnt += 1
                            if binggo_cnt == 3 :
                                return

def check(m, n) :
    for i in range(3):
        for j in range(3):
            if paper[i][j] == call[m][n]:
                paper[i][j] = -1
                return 1

binggo_cnt = 0
for m in range(3) :
    for n in range(3) :
        check(m, n)
        binggo_cnt = 0
        binggo_check(paper)
        if binggo_cnt == 3 :
            print(m * 3 + n + 1)
            break
    if binggo_cnt == 3:
        break