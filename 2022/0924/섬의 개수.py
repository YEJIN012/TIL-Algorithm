import sys
sys.setrecursionlimit(50*50)

def dfs(i, j) :
    island[i][j] = 0                    # 방문한 땅은 0으로 지워주기.
    for k in range(8) :
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<h and 0<=nj<w and island[ni][nj] == 1 :
            dfs(ni, nj)


while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    else :
        island = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0
        di = [0, 1, 0, -1, 1, -1, -1, 1]
        dj = [1, 0, -1, 0, 1, 1, -1, -1]
        for i in range(h) :
            for j in range(w) :
                if island[i][j] == 1 :   # 방문하지 않은 땅 찾기.
                    dfs(i,j)             # 연결된 땅을 다 돌고 빠져나오면,
                    cnt += 1             # 섬 갯수 +1
        print(cnt)