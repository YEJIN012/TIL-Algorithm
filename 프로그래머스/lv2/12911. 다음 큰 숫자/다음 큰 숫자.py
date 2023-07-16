def solution(n):
    
# 다른 진수의 문자열로 변환
# b = format(test_value, 'b')			# 10 to 2
# o = format(test_value, 'o')			# 10 to 8
# h = format(test_value, 'x')			# 10 t0 16
    
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
