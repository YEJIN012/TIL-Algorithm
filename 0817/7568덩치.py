N = int(input())
x = [0] * N     # 몸무게 리스트
y = [0] * N     # 키 리스트

for i in range(N) :
    x[i], y[i] = map(int,input().split())

result = [1] * N                                # 등수 리스트(전체 요소를 1로 세팅)
for i in range(N) :
    for j in range(N) :
        if i != j :                             # 본인 외에 인덱스 모두 검사.
            if x[i] < x[j] and y[i] < y[j] :    # 키, 몸무게 다 큰 사람이 있으면
                result[i] += 1                  # 등수 +1

print(*result)                                  # Asterisk로 언패킹 출력.