def solution(n, words):
    person = 1
    order = 1
    last = [words[0]]
    for i in range(1, len(words)) :
        person = i % n + 1
        order = i // n + 1
        if words[i][0] == last[-1][-1] :
            if words[i] in last:
                answer = [person, order]
                break
            else :
                last.append(words[i])
        else :
            answer = [person, order]
            break
            
    else :
        answer = [0,0]

    return answer