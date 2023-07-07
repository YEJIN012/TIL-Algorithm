def solution(n):
    b = format(n, 'b')
    k = 0
    for bb in b :
        if bb == '1' :
            k += 1
    
    next_k = -1
    while next_k != k :
        n += 1
        next_b = format(n, 'b')
        next_k = 0
        for bb in next_b :
            if bb == '1' :
                next_k += 1
    
    answer = n
    return answer