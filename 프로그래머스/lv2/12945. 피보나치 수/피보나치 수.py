def solution(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    
    else :
        a = 0
        b = 1
        while n > 1 :
            answer  = a + b
            a = b
            b = answer
            n -= 1
        return answer % 1234567