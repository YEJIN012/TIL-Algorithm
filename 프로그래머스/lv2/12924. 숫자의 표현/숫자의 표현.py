def solution(n):
    nums = list(range(1, n+1))
    cnt = 0
    for i in range(n-1, -1, -1) :
        for j in range(i+1, n+1) :
            # print(nums[i:j])
            if sum(nums[i:j]) == n :
                cnt += 1
                break
            elif sum(nums[i:j]) > n :
                break
    return cnt