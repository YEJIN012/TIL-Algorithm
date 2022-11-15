# 플러스를 다 계산해주고 마이너스를 마지막에 순차적으로 계산하는 것 -> 최솟값

minus_split = list(input().split('-'))  # 마이너스 기준으로 식 분할.
plus_value = []
for i in minus_split  :                  # 플러스로 구성된 식들을 다 계산하여
    num = i.split('+')
    plus_ans = 0
    for j in num :
        plus_ans += int(j)
    plus_value.append(plus_ans)  # 리스트에 담아준다.

ans = plus_value[0]
for i in range(1, len(plus_value)) : # 계산된 값들에 남은 마이너스 계산.
    ans -= plus_value[i]

print(ans)






