numbers = [0,0,0,0]
answer = ''

str_numbers = list(map(str, numbers))
# print(str_numbers)

str_numbers.sort(key = lambda x : x[0], reverse=True)
# print(str_numbers)



while str_numbers :
    p = str_numbers[0][0]
    ss = [str_numbers.pop(0)]
    while str_numbers and str_numbers[0][0] == p :
        ss.append(str_numbers.pop(0))
    else :
        N = len(ss)
        for i in range(N-1, 0, -1) :
            for j in range(i) :
                if len(ss[j]) == len(ss[j+1]) :
                    if int(ss[j]) < int(ss[j+1]) :
                        ss[j], ss[j+1] = ss[j+1], ss[j]

                elif len(ss[j]) > len(ss[j+1]) :
                    temp = ss[j + 1]
                    for k in range(len(ss[j])-len(ss[j+1])) :
                        t = 0
                        temp += ss[j][t]
                        t += 1
                    if int(ss[j]) < int(temp):
                        ss[j], ss[j + 1] = ss[j + 1], ss[j]
                    elif int(ss[j]) == int(temp):
                        if ss[j][1] > ss[j+1][0] :
                            ss[j], ss[j + 1] = ss[j + 1], ss[j]


                elif len(ss[j]) < len(ss[j+1]) :
                    temp = ss[j]
                    for k in range(len(ss[j+1])-len(ss[j])) :
                        t = 0
                        temp += ss[j+1][t]
                        t += 1
                    if int(temp) < int(ss[j+1]):
                        ss[j], ss[j + 1] = ss[j + 1], ss[j]
                    elif int(ss[j+1]) == int(temp):
                        if ss[j][0] > ss[j+1][1] :
                            ss[j], ss[j + 1] = ss[j + 1], ss[j]
    # print(ss)

    for i in ss :
        answer += i
    if answer[0] == '0' :
        answer = 0
print(answer)



