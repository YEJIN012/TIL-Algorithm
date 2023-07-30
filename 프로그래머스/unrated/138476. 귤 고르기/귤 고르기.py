def solution(k, tangerine):
    max_size = max(tangerine)   # max_size : 보유 중인 귤 중 최대 사이즈
    t_size = [0] * (max_size+1) # 사이즈를 index로 가지는 0 리스트 
    for i in tangerine :        # 사이즈별 귤의 수 카운트
        t_size[i] += 1
    size_sum = list((idx, t) for idx, t in enumerate(t_size))   # size_sum : (사이즈, 갯수) 형태 튜플을 원소로 가지는 리스트
    sort_size_sum = sorted(size_sum, key=lambda x: x[1], reverse=True)  # 갯수가 많은 순서대로 size_sum 정렬
    
    answer = 0  # sort_size_sum의 인덱스 (sort_size_sum : 사이즈가 같은 귤끼리 모아놓은 리스트)
    total = 0   # 상자에 담은 귤의 수
    while True :
        if k - total > sort_size_sum[answer][1] :   # 모아놓은 귤 전체를 담아도 k를 넘지않으면, 
            total += sort_size_sum[answer][1]       # 담고 진행.
        else :                                      # 아니면 해당 사이즈의 귤 일부만 담게 되므로,
            answer += 1                             # 사이즈 종류만 +1
            break                                   # 종료.
        
        answer += 1 # 첫번째 사이즈 -> 0 idx 고려
    
    return answer