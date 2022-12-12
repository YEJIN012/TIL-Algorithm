import collections as col
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
answer = ''
participant_dic = col.Counter(participant)  # list 원소를 키로 받고 중복값이 있을 경우 카운트하여 value값으로 받는 dict생성
for i in completion :               # 완주자 명단의 선수를 한 명씩
    participant_dic[i] -= 1         # 참석자dict 명단(key) value값에서 1씩 빼준다.

for i,j in participant_dic.items() :# i = 참석자 선수 이름, j = 완주자를 확인 하고 남음 value값
    if j == 1 :                     # 참석자명단에 남은 선수는
        answer = i                  # 완주하지 못한 선수.

print(answer)

# 카운트없이 list를 그대로 dict형으로 바꿈
participant_dict = {x : 1 for x in participant}
# participant_dict = {participant[i] : 1 for i in range(0,len(participant))}
print(participant_dict)
# count method를 사용하여 list 원소를 키로 받고 중복값이 있을 경우 카운트하여 value값으로 받는 dict생성
participant_dic2 = {x : participant.count(x) for x in participant}
print(participant_dic2)



# 알고리즘 상관없이 dictionary가 list보다 최소 수십 배 이상 빠르므로
# 자료형만 바꾸셔도 무난히 통과됩니다.

# 싹 다 시간초과 ;;;;
# for i in participant :
#     if i in completion :
#         k = completion.index(i)
#         completion[k] = 0
#     else :
#         answer = i
# print(answer)

# for i in completion :
#     k = participant.index(i)
#     participant.pop(k)
# for i in participant :
#     answer = i
# print(answer)
