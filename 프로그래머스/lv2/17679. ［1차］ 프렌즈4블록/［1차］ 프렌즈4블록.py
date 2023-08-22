def solution(m, n, board):
    answer = 0  # 지워지는 총 블록 수.
    arr = [0] * m   # 각 블록의 문자를 가지는 이차원배열
    for i, line in enumerate(board) :
        a = []
        for j in line :
            a.append(j)
        arr[i] = a
    
    while True :    # 2x2 문자가 생길 때까지 반복.
        # STEP 1
        deleteB = set() # 한 판에서 지워질 수 있는 블록 {(i,j)} 집합
        for i in range(m-1) :
            for j in range(n-1) :
                block = arr[i][j]
                for di, dj in [(0,1), (1,1), (1,0)] :   # arr[i][j]를 기준으로 2x2배열 문자 조회
                    ni = i+di
                    nj = j+dj
                    if not 'A' <= block <= 'Z' or arr[ni][nj] != block:
                        break
                else :
                    deleteB.update([(i, j),(i,j+1),(i+1,j),(i+1,j+1)])  # 4칸의 문자가 모두 같으면 deleteB 집합 update             
        answer += len(deleteB)  # 지울 수 있는 블록 갯수 추가.
        
        
        if deleteB :    # 지울 수 있는 블록이 있으면, 진행
            # STEP 2
            for deli, delj in deleteB :
                arr[deli][delj] = ''   # 지워지는 블록을 arr배열에서 ''로 표기
        
            # STEP 3
            
            ### test case 5,6,10,11 실패 ###
            # for i in range(m-1, -1, -1) :   # 위에서부터 블록이 떨어지므로 아래 배열에서 위로 역진행.
            #     for j in range(n-1, -1, -1) :
            #         if arr[i][j] == '' :   # 지워진 블록을 찾으면,
            #             k = -1
            #             while 0<=i+k :    # 해당 블록 기준에서 윗블록 중에서
            #                 if arr[i+k][j] != '' : # 지워지지않은 블록 찾기.
            #                     arr[i][j] = arr[i+k][j] # 해당 블록이 떨어진걸로 생각.
            #                     arr[i+k][j] = ''       # 떨어진 블록은 비어있는걸로 표시.
            #                 else :
            #                     k -= 1
            
            for j in range(n) :   
                for i in range(m-2, -1, -1) :   # 위에서부터 블록이 떨어지므로 아래 행에서 위로 역진행.
                    if arr[i][j] == '' :
                        continue
                        
                    # 남아있는 블록을 찾으면,
                    for k in range(m-1, i, -1) :    # 해당 블록 기준 맨아래에서부터 위로 올라오며 조회.
                        if arr[k][j] == '' :       # 지워진 블록들은
                            arr[k][j] = arr[i][j] # 해당 블록이 떨어진걸로 생각.
                            arr[i][j] = ''       # 떨어진 블록은 비어있는걸로 표시.
                            break

                    
        else :
            break
            
    return answer