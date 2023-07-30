# dp
def solution(land):
    for i in range(0, len(land)-1) :
        next = land[i+1][:] # 다음 행의 원본을 복사
        for j in range(4) :
            for n in range(4) :
                if j != n : # 현재 열과 같지 않은 열만
                    get = land[i][j] + next[n] # 현재 땅의 값 + 다음 땅의 값 누적
                    land[i+1][n] = get if get > land[i+1][n] else land[i+1][n]  # 누적 최대 값 갱신
            
    return max(land[-1])