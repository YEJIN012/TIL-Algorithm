def f(board):
    cnt1 = 0    # (0,0)를 B로 만드는 경우, 다시 칠하는 횟수
    cnt2 = 0    # (0,0)를 A로 만드는 경우, 다시 칠하는 횟수
    # (0,0)를 B로 만드는 경우
    pre = 'W'                           # 왼쪽 칸 (행이 바뀔 때는 전 행의 끝열 반대색) 의 색깔
    for m in range(8):
        for n in range(8):
            if board[m][n] != pre :     # pre와 반대이면 통과
                pre = board[m][n]       # 현재 칸 색을 pre에 넣고 탐색 계속.
            else :                      # pre와 같으면
                pre = 'B' if board[m][n] == 'W' else 'W'    # pre에 현재칸과 반대색 저장 (다시 칠해줬다는 개념)
                cnt1 += 1               # 다시 칠하는 횟수 +1

        pre = 'B' if pre == 'W' else 'W'    # 행이 바뀌고 [0]열은 이전 행 끝열[7]의 색과 같아야 하므로 pre에 반대 색생을 넣어줌.

    # (0,0)을 W로 만드는 경우
    pre = 'B'
    for m in range(8):
        for n in range(8):
            if board[m][n] != pre :
                pre = board[m][n]
            else :
                pre = 'B' if board[m][n] == 'W' else 'W'
                cnt2 += 1

        pre = 'B' if pre == 'W' else 'W'

    return cnt1 if cnt1 < cnt2 else cnt2    # 두 값 중 작은 값 리턴.


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
minV = 2500
for i in range(N-7):
    for j in range(M-7):                    # 모든 칸을 순회하며
        arr_cut = [0] * 8                   # 8*8로 자른 이차원배열
        k = 0
        for ii in range(i,i+8) :
            arr_cut[k] = arr[ii][j:j+8]
            k += 1
        cnt = f(arr_cut)                    # 다시 칠해야 하는 최솟값 구하는 함수.
        if minV > cnt :                     # 모든 칸마다 최솟값 갱신
            minV = cnt
print(minV)
