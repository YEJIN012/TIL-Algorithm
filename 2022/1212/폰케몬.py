# 폰켓몬

# nums = [3,3,3,2,2,4]
nums = [3,3,3,2,2,2]
dict = {i : nums.count(i) for i in nums}
if len(nums)//2 > len(dict) :   # 전체 폰켓몬 수 / 2 보다 전체 폰켓몬 종류의 번호 수가 적으면,
    answer = len(dict)          # 가질 수 있는 폰켓몬 종류 수의 최댓값 = 전체 폰켓몬 종류의 번호 수
else :                          # 아니면,
    answer = len(nums)//2       # 각각 다른 종류의 폰켓몬을 (전체 폰켓몬 수 / 2)마리 고르면 된다. 그게 최댓값.
print(answer)