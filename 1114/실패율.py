def solution(N, stages):
    answer = []
    # index:0 제외, N+1도 일단 그냥 담아줌.
    nonclear = [0] * (N+2)      # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
    allonstage = [0] * (N+2)    # 스테이지에 도달한 플레이어 수
    for i in stages :
        for j in range(1,i+1):
            allonstage[j] += 1
        nonclear[i] += 1


    failure = []
    for i in range(1, N+1) :
        if allonstage[i] == 0 :
            failure.append((i,0))   # 튜플 형태로 인덱스와 함께 실패율을 담는다.
        else :
            failure.append((i,nonclear[i] / allonstage[i]))
    # print(failure)


    # answer = sorted(failure, key = lambda x: x[1], reverse=True)
    # .sort()와 동일한 코드
    failure.sort(key = lambda x: x[1], reverse=True)    # 실패율 x[1]을 기준으로 sort
    # print(failure)
    for i in failure :
        answer.append(i[0])                             # 정렬된 배열의 인덱스만 answer에 담는다
    # print(answer)
	return answer