def solution(s):
    zero = 0    # 제거된 0의 갯수
    time = 0    # 이진 변환 룃수
    while s != '1' :    # s가 '1'이 될 때까지
        onlyone = 0     # '1'의 갯수
        for idx, zeroone in enumerate(s) :
            if zeroone == '1' :
                onlyone += 1
            else :
                zero += 1
        s = str(format(onlyone, 'b'))   # 이진 변환
        time += 1   # 변환 횟수 증가
    return [time, zero]