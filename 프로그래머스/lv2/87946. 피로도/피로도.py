# 최대한 많은 던전
# 유저 보유 피로도 >= 최소 필요 피로도 + 소모 피로도
from itertools import permutations
def solution(k, dungeons):
    # dungeons = sorted(dungeons, key=lambda x:x[0], reverse = 1)
    max_cnt = 0 # 최대 탐험 횟수
    cpr = list(permutations(dungeons, len(dungeons)))
    for i, m in enumerate(cpr) :
        P = k   #  최초 피로도
        cnt = 0
        for j, n in enumerate(m) :
            n_P, u_P = n    # 최소필요피로도, 소모피로도
            if P >= n_P :
                cnt += 1
                P -= u_P
            else :
                break
        max_cnt = cnt if max_cnt < cnt else max_cnt
        if max_cnt ==  len(dungeons) :
            break
        
    return max_cnt