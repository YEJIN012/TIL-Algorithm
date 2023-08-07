# 0층에서 storey층까지 올라간다고 생각한다.
# "0보다 작으면 엘리베이터는 움직이지 않습니다." 이므로, storey층을 넘어가면 안된다고 생각한다.
# tase case: 1,3,12 -> 현재(i) 자리가 5이면 i-1 자리가 5이상인지 미만인지에 따라 올림 고려.
#                   -> 9일 때도 고려, 그 다음 i-2 자리 수에 +1, i-1 은 0.

def solution(storey):
    answer = 0
    num_storey = [0] + [int(i) for i in str(storey)]    # 주어진 수의 최상위 자리보다 큰 자리수를 0으로 하는 각자리 수를 원소로 가지는 배열 세팅. ex) 2554 -> [0,2,5,5,4]
    N = len(num_storey)
    
    for i in range(N-1, -1, -1) : # 일의자리수 부터 조회.
        print(num_storey[i])
        if num_storey[i] >= 6 or (num_storey[i] == 5 and num_storey[i-1] >= 5) :
        # 6 이상이면, 앞자리수를 올림하고 10-n 만큼 내려오는 것이 최소값이 되는 방법.
        # 또는 5일 때는 그 앞자리수를 같이 고려. 앞자리 수가 5이상이면 올림 아니면 내림.
            if num_storey[i-1] == 9 :
                num_storey[i-1] = 0
                num_storey[i-2] += 1
            else :
                num_storey[i-1] += 1
            answer += 10-num_storey[i]
            
        else :  # 5 미만이면, 그냥 n만큼 올라가는 것이 최소값이 되는 방법.
            answer += num_storey[i] 
        
    return answer