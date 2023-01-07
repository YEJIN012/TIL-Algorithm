def nonselfnum(n) :
    ans = 0
    ans += n
    if n >= 1000 :
        ans += n // 1000
        n = n % 1000

    if n >= 100 :
        ans += n // 100
        n = n % 100

    if n >= 10 :
        ans += n // 10
        n = n % 10

    ans += n

    return ans

n = 1
selfnum = [0] * 10001
while n <= 10000 :                  # n이 커질때 함수값도 차례로 커지지 않으므로, n을 10000까지는 다 돌려봐야 함.
    if nonselfnum(n) <= 10000 :
        selfnum[nonselfnum(n)] += 1
    n += 1

for i in range(1, 10001) :
    if selfnum[i] == 0 :
        print(i)


