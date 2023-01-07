N = int(input())
numbers = list(int(input()) for _ in range(N))

### 시간초과 ###
# for i in range(N-1,0,-1): # 버블정렬
#     for j in range(i) :
#         if numbers[j] > numbers[j+1] :
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#
#
# for i in numbers:
#     print(i)  # 정렬된 요소들을 list에서 차례로 꺼내 한줄씩 출력.


### 시간초과 ###
for i in range(1,N+1): # 역순 버블정렬로 바로바로 출력.
    for j in range(N-1,i-1,-1) :
        if numbers[j] < numbers[j-1] :
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

    print(numbers[i-1])
