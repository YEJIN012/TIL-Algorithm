def solution(elements):
    N = len(elements)
    answer = 0
    sum_list = {}
    for k in range(1, N+1) :
        for i in range(N) :
            if i+k <= N :
                sum_list[sum(elements[i:i+k])] = 1
            else :
                # 7 9 1 1 4
                sum_list[sum(elements[i:]) + sum(elements[:(i+k)%N])] = 1
    return len(sum_list.keys())