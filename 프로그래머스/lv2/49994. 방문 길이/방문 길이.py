def solution(dirs):
    rotate = {
        'U' : [-1,0,0,1],   # 이동방향 + rotate(index) + 반대길rotate(index)
        'D' : [1,0,1,0],
        'R' : [0,1,2,3],
        'L' : [0,-1,3,2]
    }
    # 하나의 좌표당 [UDRL] 각 방향으로 이동하는 로드의 방문횟수를 담는 배열을 가지고 있다.(3차원배열)
    # 가장 모서리의 좌표에서의 존재하지 않는 길은 -1로 설정.
    arr = [[[-1,0,0,-1]]+[[-1,0,0,0]for _ in range(9)]+[[-1,0,-1,0]]] + [[[0,0,0,-1]]+[[0] * 4 for _ in range(9)]+[[0,0,-1,0]] for _ in range(9)] + [[[0,-1,0,-1]]+[[0,-1,0,0]for _ in range(9)]+[[0,-1,-1,0]]]
    i, j = (5,5)
    for dir in dirs :
        di, dj, r, nr = rotate[dir]
        ni = i + di
        nj = j + dj
        if 0<=ni<11 and 0<=nj<11 :
            arr[i][j][r] = 1
            arr[ni][nj][nr] = 1
            i, j = ni, nj
    ans = 0
    for i, row in enumerate(arr) :
        for j, c in enumerate(row) :
            for k, time in enumerate(c) :
                if time == 1 :
                    ans += 1
    return ans//2