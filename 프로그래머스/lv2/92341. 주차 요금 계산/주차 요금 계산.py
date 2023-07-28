# fees : 기본시간, 기본요금, 단위시간, 단위요금
# records : 시각, 차량번호, 내역
# 하루에 입차를 두 번 할 수도 있음.

# 차량번호를 조회하기 위해서는 dictionary가 유리하고
# 차량번호 정렬을 위해서는 list여야 한다.
def solution(fees, records):
    parking = {}    # 입차 딕셔너리 = {차량번호 : [입차시간, 누적 주차시간]}
    for idx, record in enumerate(records) :
        rlist = list(record.split(' '))     # rlist = ['시간', '차량번호', '입출차여부']
        tlist = tuple(map(int, rlist[0].split(':'))) # tlist = (시, 분)
        time = tlist[0]*60 + tlist[1]
        if rlist[1] in parking.keys() :     # 이전 기록이 있다면
            if rlist[2] == 'OUT' :  # 출차이면,
                parking[rlist[1]][1] += time - parking[rlist[1]][0] # 기존 입차시간과 누적시간 계산
                parking[rlist[1]][0] = -1    # 입차시간 리셋
            else :
                parking[rlist[1]][0] = time
        else :
            parking[rlist[1]] = [time, 0]
        print(rlist)
    print(parking)
    answer = []     # answer = [[ 차량번호, 총 요금 ]]
    for number in parking.keys() :
        if parking[number][0] == -1 :
            answer.append([number, parking[number][1]])
        else :
            parking[number][1] += 23*60 + 59 - parking[number][0]
            answer.append([number, parking[number][1]])
    answer = sorted(answer, key = lambda x : x[0])
    print(answer)
    for idx, ans in enumerate(answer) :
        if ans[1] <= fees[0] :
            answer[idx] = fees[1]
        else :
            order = 1 if (ans[1]-fees[0])%fees[2] > 0 else  0
            answer[idx] = fees[1] + ((ans[1]-fees[0])//fees[2] + order) * fees[3] 
    print(answer)
    return answer