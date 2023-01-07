import sys

short = [int(sys.stdin.readline()) for _ in range(9)]
seven_short = [0] * 7
for a in range(8) :                         # 7명 중에 배제할 두명(a,b) 완전탐색.
    total = 0
    for b in range(a+1, 9) :
        total = 0
        k = 0
        for i in range(9) :
            if i != a and i != b :          # a,b 외에 다른 애들 키 합산 구하기
                seven_short[k] = short[i]
                total += short[i]
                k += 1
        if total == 100 :                   # 합산 100 나오면 탐색 종료.
            break
    if total == 100 :
        break

for i in range(6, 0, -1) :                  # 오름차순 배열
    for j in range(i) :
        if seven_short[j] > seven_short[j+1] :
            seven_short[j], seven_short[j+1] = seven_short[j+1], seven_short[j]

for i in range(7) :
    print(seven_short[i])
