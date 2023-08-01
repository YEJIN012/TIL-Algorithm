def solution(n):
    nums = list(range(1, n+1))
    cnt = 0
    # 1부터 n까지 모든 부분집합의 합을 구한다.
    for i in range(n) :
        for j in range(i+1, n+1) :
            if sum(nums[i:j]) == n :    # 합이 n이 되면 cnt +1 후, 중단.
                cnt += 1
                break
            elif sum(nums[i:j]) > n :   # 합이 n을 이미 넘으면 중단.
                break
    return cnt
