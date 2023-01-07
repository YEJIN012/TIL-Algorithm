word = input()                 # 입력 받은 문자열
word = list(word.upper())            # 대문자로 통일
Alphabet = list(set(word))           # 문자열 중복제거.

Max = 0
same = 0                            # 가장 많이 사용된 알파벳이 여러 개 존재하는지 확인 인자.
A = 0                               # 가장 많이 사용된 알파벳

for i in range(len(Alphabet)) :     # 사용된 각각의 알파벳 갯수 카운트.
    cnt = 0
    for j in range(len(word)) :
        if word[j] == Alphabet[i] :
            cnt += 1
    if Max < cnt :                  # 가장 많이 사용된 알파벳 구하기.
        Max = cnt
        A = Alphabet[i]
        same = 0
    elif Max == cnt :               # 가장 많이 사용된 알파벳 같은 갯수의 알파벳이 있으면 same +1
        same = 1

if same :
    print('?')
else :
    print(A)