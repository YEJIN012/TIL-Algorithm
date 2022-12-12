phone_book = ["12","123","1235","567","88"]

# dict를 한번에 만들 생각하지 말고, for문 돌면서 key와 value값 add가능.
# 가능한 모든 접두어 경우를 key로 받는 딕셔너리를 만들면 -> 1,000,000 * 19(본인을 제외한 최대 전화번호길이) loop
s = dict()                      # 빈 딕셔너리 생성
for i in phone_book :           # 전화번호 리스트를 순회하면서
    for j in range(1, len(i)) : # 스스로(s[i])를 제외하고
        s[i[0:j]] = 1           # 자신이 만들 수 있는 모든 접두사를 key로 만듦.
                                # (value값은 의미없음. 중복이여도 그냥 1)

for i in phone_book :           # 전화번호부에 적힌 전화번호가
    if i in s :                 # 접두사 dict에 존재하면,
        answer = False          # 어떤 번호가 다른 번호의 접두어가 된다는 뜻.
print(answer)

# 시간초과
# 한 번호당 전체 전화번호를 순회하면 -> 1,000,000 * 1,000,000 loop
# dic = {x : 0 for x in phone_book}
# answer = True
# for i in dic :
#     k = 0
#     for j in dic :
#         if i == j[0:len(i)] :
#             k += 1
#         if k > 1 :
#             answer = False
#             break
#     if answer == False :
#         break
