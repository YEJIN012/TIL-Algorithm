N, M = map(int,input().split())
cards = list(map(int, input().split()))
sum_list = []

for i in range(N-2) : # 3개의 원소의 합 전체 경우의 수. sum_list
    for j in range(i+1,N-1) :
        for k in range(j+1,N) :
            sum_list.append(cards[i] + cards[j] + cards[k])

sum_list.sort() # 오름차순으로 정렬

if sum_list[len(sum_list)-1] < M : # 가장 마지막 값이 M보다 작으면, 마지막 값 바로 출력.
    print(sum_list[len(sum_list)-1])

else :
    for i in range(len(sum_list)) : # 아니면, 합 리스트 전체 순서대로 탐색.

        if sum_list[i] == M : # M과 같은 값이 나오면, 해당값 바로 출력.
            print(sum_list[i])
            break

        elif sum_list[i] > M : # 합이 M보다 커지는 순간, 바로 직전 값 출력.
            print(sum_list[i-1])
            break