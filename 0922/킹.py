king, stone, N = input().split()                    # 초기 입력값 : [열][행]
trans = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
trans_move = {'R' : (0,1), 'L' : (0,-1), 'B' : (1,0), 'T' : (-1,0), 'RT' : (-1,1), 'LT' : (-1,-1), 'RB' : (1,1), 'LB' : (1,-1)}
K = (8 - int(king[1]), trans.get(king[0]))          # 킹위치(행,열) = ( king[1] 숫자반전, king[0] 문자교환 )
stone = (8 - int(stone[1]), trans.get(stone[0]))    # 돌위치(행,열) = ( stone[1] 숫자반전, stone[0] 문자교환 )

i, j = K
si, sj = stone
for _ in range(int(N)) :                            # N번 이동.
    di, dj = trans_move.get(input())                # 이동값(문자) 행렬(튜플)로 교환
    ni, nj = i+di, j+dj
    if 0<=ni<8 and 0<=nj<8 :                        # 킹 이동 위치가 범위 이내이면,
        if ni == si and nj == sj :                      # 돌 위치와 겹치는지 확인.
            nsi, nsj = si + di , sj + dj                # 겹치면, 돌도 똑같이 이동.
            if 0<=nsi<8 and 0<=nsj<8 :                      # 돌 이동 위치가 범위 이내이면,
                si = nsi                                    # 돌과 킹 모두 이동.
                sj = nsj
                i = ni
                j = nj
        else :                                          # 킹 이동 위치가 돌 위치와 겹치지 않으면,
            i = ni                                      # 돌만 이동.
            j = nj

for key, value in trans.items() :                  # value값으로 key 찾는 포문.
    if value == j :
        j = key
    if value == sj :
        sj = key
print(f'{j}{8-i}')
print(f'{sj}{8-si}')
