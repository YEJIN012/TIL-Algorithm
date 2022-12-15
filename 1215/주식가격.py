prices = [1,4,2,3,5,4,1,2,3]
answer = []
answer = [0] * len(prices)

for i in range(len(prices)-1) :
    t = 0
    for j in range(i+1,len(prices)) :
        t += 1      # 1초 뒤에 가격이 떨어져도 1초간은 가격이 떨어지지 않은 것이므로, 다음 가격에 상관없이 무조건 1초 플러스.
        if prices[i] > prices[j] :  # 다음 가격이 떨어지면,
            break   # t 늘리는거 중단.
    answer[i] = t
print(answer)
# [8, 1, 4, 3, 1, 1, 2, 1, 0]