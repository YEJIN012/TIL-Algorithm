from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 :    # 전체 합이 홀수이면, 불가
        return -1

    q_a = deque(queue1)
    # s_b = deque(queue2) # 최초 queue2 보존
    q_b = deque(queue2)
       
    totalA = sum(queue1)
    totalB = sum(queue2)
    target = (totalA + totalB) // 2
    answer = -1
    
    # 매번 sum(queue)로 계산해주면 시간초과...
    # 최초 total값을 생성해준후 queue의 총합은 해당 total에서 append(+) pop(-) 되는 값만 계산해줘야 한다.
    # queue1을 기준으로 target(반값)을 맞춰주면 되므로,
    # queue2에 뺄때는 queue1으로 옮겨주고
    # queue1에서 뺄때는 그냥 빼주기만 한다.
    # -> queue2에 남은 것이 없다는 것은 queue1이 모두 queue2의 원소로만 채워졌다는 것. (q_a == s_b)
    cnt = 0
    while q_b : # queue2가 비워있지 않으면,
        if totalA == target :
            answer = cnt
            break
        
        if totalA < target :
            k = q_b.popleft()
            totalA += k
            q_a.append(k)
        else :
            k = q_a.popleft()
            totalA -= k
        cnt += 1

    return answer
        