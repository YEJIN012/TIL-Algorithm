def solution(k, tangerine):
    max_size = max(tangerine)
    t_size = [0] * (max_size+1)
    for i in tangerine :
        t_size[i] += 1
    size_sum = list((idx, t) for idx, t in enumerate(t_size))
    sort_size_sum = sorted(size_sum, key=lambda x: x[1], reverse=True)
    
    answer = 0
    total = 0
    while True :
        if k - total > sort_size_sum[answer][1] :
            total += sort_size_sum[answer][1]
        else :
            answer += 1
            break
        
        answer += 1
    
    return answer