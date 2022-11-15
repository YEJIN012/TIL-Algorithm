S = input()
minV = len(S)
for k in range(1,len(S)//2+1) :
    newS = ''
    i = 0
    string = S[i:i+k]
    repeat = 1
    i += k
    while i+k <= len(S) :
        while string == S[i:i+k] :
            repeat += 1
            i += k
        else :
            if repeat > 1 :
                newS += str(repeat)
                repeat = 1
                newS += string
                string = S[i:i+k]
                i += k
            else :
                newS += string
                string = S[i:i+k]
                i += k
    else :
        newS += string
        newS += str(S[i:])

    if len(newS) < minV :
        minV = len(newS)
print(minV)


