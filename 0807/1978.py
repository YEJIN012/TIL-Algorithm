N = input()
numbers = list(map(int,input().split()))

prime_numbers = []
for i in numbers :
    s = 2
    if i  == 1 :
        pass
    elif i == 2 :
        prime_numbers.append(2)
    else :
        for s in range(2,i) :
            if i % s == 0 :
                break
            else :
                if s == i-1 :
                    prime_numbers.append(i)

print(len(prime_numbers))