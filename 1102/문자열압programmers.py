def solution(s):
    minV = len(s)
    for k in range(1,len(s)//2+1) :     # 2번이상 반복되어야하므로 1개 단위부터 (전체문자열//2)개 단위까지 전체탐색
        news = ''   # 새로운 문자열
        i = 0
        string = s[i:i+k]       # 반복되는지 확인하는 문자열 string
        repeat = 1              # 반복되는 횟수 (자기자신 하나만 있어도 1)
        i += k                  # 다음 문자열부터 확인.

        while i+k <= len(s) :   # 문자열(string)인덱스가 범위안에 있어야하므로 i+k
            while string == s[i:i+k] :  # string이 반복되면
                repeat += 1             # repeat +1 반복
                i += k
            else :                      # 반복이 깨지면,
                if repeat > 1 :         # repeat이 1초과인지 확인.
                    news += str(repeat) # repeat횟수 새문자열에 넣어주고
                    repeat = 1          # repeat 초기화
                    news += string      # 반복된 문자열 넣어주고
                    string = s[i:i+k]   # 반복되는지 확인하는 문자열을 다음 문자열로 다시 지정.
                    i += k
                else :                  # repeat이 1이면,
                    news += string      # string만 넣어주고
                    string = s[i:i+k]   # 반복되는지 확인하는 문자열을 다음 문자열로 다시 지정.
                    i += k
        else :                          # 전체 문자열 범위가 끝나면
            news += string              # 확인 못하고 남은 문자열 받아주고
            news += str(s[i:])          # 그 뒤에 남은 문자열도 끝까지 다 받아줌.

        if len(news) < minV :           # 가장 작은 압축 크기 갱신.
            minV = len(news)

    answer = minV
    return answer