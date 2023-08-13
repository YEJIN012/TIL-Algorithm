def solution(n,a,b):
    cnt = 1
    # while abs(a-b) != 1 : # 이면, 참가자 번호 2 3 을 부여 받았을 때도 대결하는 것으로 판단하므로 안됨.
    while True :
        if abs(a-b) == 1 and a//2 != b//2 : # 1 2 또는 13 14 식으로 참가자 번호 1 차이가 나고 2로 나눈 몫이 다를 때 만나게 된다.
            break
        if a % 2 == 1 :
            a = a // 2 + 1
        else :
            a = a // 2
        if b % 2 == 1 :
            b = b // 2 + 1
        else :
            b = b // 2
        cnt += 1
    
    return cnt