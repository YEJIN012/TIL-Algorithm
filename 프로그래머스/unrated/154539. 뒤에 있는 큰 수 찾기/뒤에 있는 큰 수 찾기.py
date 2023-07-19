def solution(numbers):
    answer = [-1] * len(numbers)
    for i in range(len(numbers)-2, -1, -1) :
        for j in range(i+1, len(numbers)) :
            if numbers[i] < numbers[j] :
                answer[i] = numbers[j]
                break
            else :
                if answer[j] == -1 :
                    answer[i] = -1
                    break
                elif numbers[i] < answer[j] :
                    answer[i] = answer[j]
                    break
    return answer