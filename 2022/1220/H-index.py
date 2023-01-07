citations = [9,7,6,2,1]
answer = 0
citations.sort(reverse = True)  # 인용 횟수 내림차순 정렬
p = citations[0]    # p : 최대 인용횟수(최종 h)
i = 0               # i : p회 이상 인용된 논문의 수
while i < len(citations)-1 :    # i+1와의 비교를 위해 len(citations)-1 미만 인덱스까지만 조회.
    if p == i + 1 :             # 인용횟수 p와 p회 이상 인용된 논문의 수가 같다면,
        answer = p              # 답 = p
        break
    else :                      # 그렇지 않고,
        # H-index가 꼭 citations배열에 존재하는 값이 아닐 수 있다.
        if p != citations[i+1] :# 그 다음 논문의 인용횟수와 현재 인용 횟수가 같지 않으면,
            p -= 1              # 인용횟수만 1회 감소. 재확인.
        else :                  # 그 다음 논문의 인용횟수와 현재 인용 횟수가 같으면,
            i += 1              # 다음 논문 확인. (p회 이상 인용된 논문의 수 +1)
            p = citations[i]    # p = 다음 논문의 인용횟수

else :              # 최소 인용횟수 논문까지 도달했을시,(최소 인용횟수 >= 전체 논문수)
    if p > i+1 :    # 인용횟수 > 전체 논문수 이면,
        answer = i+1# H-index = 전체 논문수
    elif p == i+1 :
        answer = p

print(answer)

# 다른사람 풀이
# citations.sort(reverse=True)
# print(list(enumerate(citations, start=1)))  # [(2, 9), (3, 7), (4, 6), (5, 2), (6, 1)]
# # enumerate: (index, value) 튜플형으로 뽑아 나열한다. start인자 -> index 시작 값.
# # 이때 index는 현재 value값 이상 인용이 된 책의 총 갯수이다.
# print(list(map(min, enumerate(citations, start=1))))    # [1, 2, 3, 2, 1]
# # 각 튜플값 중 작은값을 뽑는다 -> value가 뽑힐 경우 -> 지금까지의 책의 총갯수 > value값 이므로 이 이후에 값들은 h번 이하 인용이 된 나머지 논문들이다.
# print(max(map(min, enumerate(citations, start=1))))     # 3
# # max값은 가능한 h값의 최대값이다.
# # 즉 h index는 'h권 이상'이 기준이어야한다.
# answer = max(map(min, enumerate(citations, start=1)))
# print(answer)