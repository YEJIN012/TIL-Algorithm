s = "(()("
answer = True

stack = []
for i in s :
    if stack :
        if i == '(' :
            stack.append(i)
        else :
            if stack[-1] == '(' :
                stack.pop(-1)
    else :
        if i == '(' :
            stack.append(i)
        else :
            answer = False
            break
else :
    if stack :
        answer = False
print(answer)