def solution(absolutes, signs):
    a = absolutes[0] if signs[0] else absolutes[0] * -1
    for i in range(1, len(signs)) :
        if signs[i] :
            a += absolutes[i]
        else :
            a -= absolutes[i]
    return a