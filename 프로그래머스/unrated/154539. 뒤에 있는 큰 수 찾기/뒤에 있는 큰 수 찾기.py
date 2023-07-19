def solution(numbers):
    answer = [-1] * len(numbers)
    for i in range(len(numbers)-2, -1, -1) :    # 뒤에 있는 (오른쪽) 수를 비교하므로, 오른쪽에서부터 역으로 내려옴.
        for j in range(i+1, len(numbers)) :     # i+1부터 오른쪽 전체 비교
            if numbers[i] < numbers[j] :            # 큰 수 등장시
                answer[i] = numbers[j]              # 바로 저장.
                break
            else :                                  # numbers[j]가 나보다 작거나 같으면, 나보다 작거나 같은 numbers[j]가 이미 찾은 뒷 큰 수와 비교
                if answer[j] == -1 :                # numbers[j]가 이미 찾은 뒷 큰 수 answer[j] 가 없으면
                    break                           # 그냥 break

                elif numbers[i] < answer[j] :       # answer[j]가 나보다도 크면
                    answer[i] = answer[j]           # 해당 값 나도 저장
                    break
    return answer


# stack 풀이방법
# : 한 번의 for문을 돌면서 idx를 stack에 담아주고
    스택에 있는 idx number값들을 while문을 돌면서 한번에 다 찾아준다.
    뒷큰수를 못 찾은 애들은 계속 stack에 남아있다. 

# def solution(numbers):
#     answer = [-1] * len(numbers)
#     stack = []

#     for ind, num in enumerate(numbers):
#         while stack and numbers[stack[-1]] < num:
#             answer[stack.pop()] = num
#         stack.append(ind)
#     return answer
