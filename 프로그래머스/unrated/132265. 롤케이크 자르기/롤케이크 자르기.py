from collections import Counter
def solution(topping):
    answer = 0
    N = len(topping)
    c_topping = set(topping[:1])
    d_topping = Counter(topping[1:])
    for i in range(2, N) :
        c_topping.add(topping[i-1])
        if d_topping[topping[i-1]] == 1 :
            d_topping.pop(topping[i-1])
        else :
            d_topping[topping[i-1]] -= 1
        if len(c_topping) == len(d_topping) :
            answer += 1
        elif len(c_topping) > len(d_topping) :
            break
        
    return answer