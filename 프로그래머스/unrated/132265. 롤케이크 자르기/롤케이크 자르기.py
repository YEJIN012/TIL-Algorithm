from collections import Counter
def solution(topping):
    answer = 0
    N = len(topping)
    
    # 형과 동생의 토핑 종류의 갯수를 모두 해시로 설정한다.
    c_topping = set(topping[:1])
    d_topping = Counter(topping[1:])    # 동생이 다 가진 상태로 시작.
    
    for i in range(2, N) :
        c_topping.add(topping[i-1]) # 형이 하나씩 가져간다. (set 중복제거로 그냥 add)
        if d_topping[topping[i-1]] == 1 :   # 동생 dict에서 하나밖에 안남은 토핑이면,
            d_topping.pop(topping[i-1])     # 아예 헤당 토핑 key pop
        else :
            d_topping[topping[i-1]] -= 1    # 1 초과이면 -1
            
        if len(c_topping) == len(d_topping) :   # 토핑 종류의 갯수를 비교.
            answer += 1
        elif len(c_topping) > len(d_topping) :  # 형의 토핑종류가 많아지는 순간 종료.
            break
        
    return answer
