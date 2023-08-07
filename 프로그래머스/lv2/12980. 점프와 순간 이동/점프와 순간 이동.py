def solution(n):
    ans = 1 # 최초 1칸 이동
    while n > 1 :
        if n % 2 == 1 :
            ans += 1
        n //= 2
    return ans