N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K) :
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
L = int(input())
direction = []                  # 방향 전환 정보 리스트.
for _ in range(L) :
    a, b = input().split()
    direction.append([int(a), b])
sec = 0
arr[0][0] = 2                   # 뱀이 있는 위치를 2로 표시.
head_i, head_j = (0,0)
D_list = [(0,1),(1,0),(0,-1),(-1,0)]    # 오른쪽으로 90도 회전 방향인자 리스트
L_list = [(0,1),(-1,0),(0,-1),(1,0)]    # 왼쪽으로 90도 회전 방향인자 리스트
di, dj = (0,1)                  # 뱀은 처음에 오른쪽을 향한다.
k = 0
snake = [(0,0)]                 # 뱀이 위치하는 칸을 받는 queue

while True :
    if sec == direction[k][0] :         # 정해진 초 시간이 오면, 방향 전환 정보 확인.
        if direction[k][1] == 'D':      # 'D'이면
            d = D_list.index((di,dj))   # 현재 방향인자에서
            di, dj = D_list[(d+1)%4]        # 오른쪽으로 90도 회전
        else :                          # 'C'이면
            l = L_list.index((di,dj))   # "
            di, dj = L_list[(l+1)%4]        # 왼쪽으로 90도 회전
        if k+1 < L :                    # 다음 주어진 방향 전환 정보 확인.
            k += 1

    ni, nj = head_i+di, head_j+dj
    # 자기자신의 몸과 부딪히지 않고, 벽에 부딪히지 않으면 이동, 계속 진행.
    if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 2  :
        sec += 1
        if arr[ni][nj] == 0 :   # 사과가 없으면,
            m,n = snake.pop(0)  # 뱀의 꼬리칸
            arr[m][n] = 0       # 0으로 지워주고 이동.
        arr[ni][nj] = 2         # 뱀이 있는 칸은 2로 표시
        snake.append((ni,nj))   # q push
        head_i, head_j = ni,nj  # 뱀머리 위치 변환.

    else :
        print(sec+1)
        break