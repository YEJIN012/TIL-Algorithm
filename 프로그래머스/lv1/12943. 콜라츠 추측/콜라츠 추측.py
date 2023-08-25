def solution(num):
    answer = 0
    while num != 1 and answer < 499 :
        if num % 2 == 0 :
            num //= 2
        else :
            num = num * 3 + 1
        answer += 1
    return answer if answer < 499 else -1