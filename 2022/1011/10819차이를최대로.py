def f(nums) :
    global maxV
    ans = 0
    for i in range(N-1) :
        ans += abs(nums[i] - nums[i+1])
    if maxV < ans :
        maxV = ans

def change(i) :
    if i == N :
        f(nums)
    else :
        for j in range(i,N) :
            nums[i], nums[j] = nums[j], nums[i]
            change(i+1)
            nums[i], nums[j] = nums[j], nums[i]

N = int(input())
nums = list(map(int, input().split()))
maxV = 0
change(0)
print(maxV)
