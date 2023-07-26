# 최대한 많은 던전
# 유저 보유 피로도 >= 최소 필요 피로도
from itertools import permutations
def solution(k, dungeons):
    cpr = list(permutations(dungeons, len(dungeons)))    # 전체 던전의 순열리스트
    
    # 경우의 수 완전탐색
    max_cnt = 0 # 최대 탐험 횟수
    for i, m in enumerate(cpr) :
        P = k   #  최초 피로도
        cnt = 0
        for j, n in enumerate(m) :
            n_P, u_P = n    # 최소필요피로도, 소모피로도
            if P >= n_P :   # 현재 피로도가 최소필요피로도 이상일 때만 다음 던전 진행 가능.
                cnt += 1
                P -= u_P
            else :
                break
                
        max_cnt = cnt if max_cnt < cnt else max_cnt    # 최대 탐험 횟수 갱신
        
        if max_cnt == len(dungeons) :    # 모든 던전을 다 돌 수 있는 경우 등장시, 탐색 종료.
            break
        
    return max_cnt
