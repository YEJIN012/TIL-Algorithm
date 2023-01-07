arr = [1,1,3,3,0,1,1]
answer = []
front_num = -1
for n in arr :
    if n == front_num :
        pass
    else :
        answer.append(n)
        front_num = n
print(answer)