def solution(brown, yellow):
    b = (brown-4) // 2
    y = 0
    x = 0
    flag = 0
    while flag == 0 :
        y += 1
        if yellow % y :
            pass
        else :
            x = yellow // y
            if x + y == b :
                flag = 1  
    
    answer = [ x+2, y+2 ]
    return answer