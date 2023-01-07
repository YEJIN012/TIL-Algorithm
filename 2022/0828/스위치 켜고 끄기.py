def change(switch, i) :
    if switch[i] == 1 :
        switch[i] = 0
    else :
        switch[i] = 1
    return switch

N = int(input())
switch = [0] + list(map(int, input().split()))
S = int(input())
for _ in range(S) :
    G, num = map(int, input().split())
    if G == 1 :
        i = num
        while i < N + 1 :
            change(switch, i)
            i += num
    else :
        change(switch, num)
        k = 1
        while num + k  < N + 1 and 1 <= num - k :
            if switch[num + k] == switch[num - k] :
                change(switch, num + k)
                change(switch, num - k)
                k += 1
            else :
                break

# result = ' '.join(map(str, switch[1:]))
for i in range(1, N + 1, 20) :
    for k in range(20) :
        if i + k < N + 1 :
            print(switch[i + k], end = ' ')
    print()