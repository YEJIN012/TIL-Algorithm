a, b = input().split()
s_a = []
s_b = []
for k in range(len(a)-1,-1,-1) :
    #세자리수에서 각자리의 수 인덱스를 역정렬하고
    s_a.append(a[k])
    s_b.append(b[k])
    # 역정렬한 자리의 수를 차례로 새로운 리스트에 받는다.

SA = int(''.join(s_a))
# 각 자리의 수는 str 형식으로 들어와 있으므로 join을 통해 세자리의 수로 만들어주고 정수로 변환시킨다.
SB = int(''.join(s_b))
sangsu = [SA, SB]
print(max(sangsu))  # 두 개의 세자리수를 하나의 리스트로 받아 max함수를 사용한다.