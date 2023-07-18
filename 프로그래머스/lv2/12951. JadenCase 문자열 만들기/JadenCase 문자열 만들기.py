def solution(s):
    s = s.lower()
    answer = ''
    idx0 = 1
    for spell in s :
        if idx0 == 1 and spell != ' ':
            spell = spell.upper()
            idx0 = 0
        elif spell == ' ' :
            idx0 = 1
        answer += spell
    
    return answer