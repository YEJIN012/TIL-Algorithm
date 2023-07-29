def solution(seoul):
    x = 0
    for idx, name in enumerate(seoul) :
        if name == 'Kim' :
            x = idx
            break
    answer = '김서방은 ' + str(x) + '에 있다'
    return answer