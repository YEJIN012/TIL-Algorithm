# def solution(s):
#     s = s.lower()
#     answer = ''
#     idx0 = 1
#     for spell in s :
#         if idx0 == 1 and spell != ' ':  
#             spell = spell.upper()
#             idx0 = 0
#         elif spell == ' ' :
#             idx0 = 1
#         answer += spell
    
#     return answer

def solution(s):
    s = s.lower()
    answer = ''
    idx0 = 1
    for spell in s :
        # if - elif 순서 중요!
        # idx0 == 1을 먼저 if로 확인하면, 문자열이 공백으로 시작하는 경우 첫단어를 대문자로 변환하지못함.
        # ex) " aaa aa" -> " Aaa Aa"
        if spell == ' ' :
            idx0 = 1
        elif idx0 == 1 :
            spell = spell.upper()
            idx0 = 0
        
        answer += spell
    
    return answer
