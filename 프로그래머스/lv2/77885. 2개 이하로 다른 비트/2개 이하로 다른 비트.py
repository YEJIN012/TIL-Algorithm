def solution(numbers):
#   test case 10,11 시간초과

#     answer = []
#    for n in numbers :
#         k = n+1
#         while True :
#             if bin(n^k).count('1') <= 2 :  # 비트(이진수)의 XOR(^) 연산자를 사용하여 다른지점 1의 갯수를 count
#                 answer.append(k)
#                 break
#             k += 1
                
#     return answer

# 이진수 특성 : n을 2로 계속 나누었을 때 결국 나머지가 0 이 되면 이진수 가장 왼쪽 비트가 0이 된다.
# 문제에서 요구하는 비트가 다른 지점이 2개 이하인 가장 작은 수는 ex) 0111 -> 1011 , 10011 -> 10101
# 처음 등장하는 0과 그 오른쪽의 1을 교체.  -> 처음 등장하는 0이 등장하기 이전(오른쪽) 비트에 해당하는 수(2^(cnt-1))를 더하는 것과 같다. 
    answer = []
    for n in numbers :
        k = n
        cnt = 0
        while k % 2 == 1:   # 이진수에서 0이 최초 등장하는 자리를 알아낸다. (이진수 오른쪽부터 왼쪽으로 진행)
            cnt += 1        # 0의 위치
            k //= 2
        answer.append(n + 2**(cnt-1) if cnt != 0 else n + 1)    # 맨 오른쪽이 최초등장하는 0의 위치이면 n+1 과 동일
        
    return answer

    
    # 한 줄 코드.....
    # return [((n ^ (n+1)) >> 2) + n + 1 for n in numbers]
