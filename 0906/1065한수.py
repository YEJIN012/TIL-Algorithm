def han(n) :
    cnt = 0
    if n <= 99 :
        cnt = n
    elif 100 <= n < 1000 :
        cnt = 99
        for k in range(100, n+1) :
            if ((k % 10) - ((k % 100) // 10)) == (((k % 100) // 10) - ((k % 1000) // 100)) :
                cnt += 1
    elif n >= 1000 :
        cnt = 144
        for k in range(1000, n+1) :
            if ((k % 10) - ((k % 100) // 10)) == (((k % 100) // 10) - ((k % 1000) // 100)) == (((k % 1000) // 100) - ((k % 10000) // 1000)) :
                cnt += 1
    return cnt

N = int(input())
print(han(N))
