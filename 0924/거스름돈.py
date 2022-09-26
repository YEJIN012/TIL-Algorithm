n = int(input())
coins = 0
if n >= 5 :             # 5보다 크면, 냅다 5로 나눠줌.
    coins = n // 5
    n = n % 5           # 5로 나눈 나머지.가
    if n % 2 == 0 :     # 2로 나누어 떨어지면 끝
        coins += n // 2
        print(coins)
    else :              # 아니면 5원짜리를 하나씩 뺴고 2원으로 줄 수 있는지 확인.
        while n > 0 :
            n += 5
            coins -= 1
            if n % 2 == 0 :
                coins += n // 2
                print(coins)
                break
        else :          # 결국 안되면 -1
            print(-1)
else :                  # 5보다 작으면 2원짜리로 해결 가능한지 확인.
    if n % 2 == 0 :
        coins += n // 2
        print(coins)
    else :
        print(-1)