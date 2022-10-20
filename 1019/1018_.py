def f(board):
    cnt = 0
    pre = board[0][0]
    for m in range(8):
        for n in range(8):
            if m == 0 and n == 0 :
                pass
            else :
                if board[m][n] != pre :
                    pass
                else :
                    board[m][n] = 'B' if board[m][n] == 'A' else 'A'
                    cnt += 1
                pre = board[m][n]
        pre = board[m][0]
    return cnt

def f2(board):
    cnt = 0
    pre = board[0][0]
    for m in range(7,-1,-1):
        for n in range(7,-1,-1):
            if m == 0 and n == 0 :
                pass
            else :
                if board[m][n] != pre :
                    pass
                else :
                    board[m][n] = 'B' if board[m][n] == 'A' else 'A'
                    cnt += 1
                pre = board[m][n]
        pre = board[m][0]
    return cnt




N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
minV = 2500
for i in range(N-7):
    for j in range(M-7):
        arr_cut = [0] * 8
        k = 0
        for ii in range(i,i+8) :
            arr_cut[k] = arr[ii][j:j+8]
            k += 1
        cnt1 = f(arr_cut)
        cnt2 = f2(arr_cut)
        cnt = cnt1 if cnt1 < cnt2 else cnt2
        if minV > cnt :
            minV = cnt
print(minV)