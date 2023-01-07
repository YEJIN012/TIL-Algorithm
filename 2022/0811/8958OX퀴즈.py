T = int(input())
for t in range(T) :
    result = input() # 퀴즈결과를 문자열 그대로 받음.
    get_score = 0 # 득점 수
    score = 1 # 연속된 정답이 나왔을 때 증가하는 해당 회차 점수 (1점부터 차례로 증가)
    for i in range(len(result)) :
        if result[i] == 'O' : # 정답이면,
            get_score += score # 회차 점수만큼 득점
            score += 1 # 다음 회차 점수는 1 증가
        else :
            score = 1 # 틀리면 회차 점수는 다시 1점

    print(get_score)