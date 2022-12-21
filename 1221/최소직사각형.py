# sizes = [[3,5],[6,2]]
# return 18

def solution(sizes):
    answer = 0
    x_sizes = sorted(sizes, key = lambda x : x[0])  # 가로값을 기준으로 오름차순 정렬.
    y_sizes = sorted(sizes, key = lambda x : x[1])  # 세로값을 기준으로 오름차순 정렬.
    print(x_sizes)
    print(y_sizes)
    x = x_sizes[-1][0]  # 가장 큰 가로값(임시)
    y = y_sizes[-1][1]  # 가장 큰 세로값(임시)
    print(x, y)

    # 전체 가로 세로 길이 중 가장 큰 값은 항상 고정.
    # 가장 큰값이 나온 쪽이 아닌 사이드의 길이를 정해야한다.
    if x > y :              # 가장 큰값이 가로면, 가로 고정.
        y = y_sizes[0][1]   # 세로를 가장 작은 값부터 차례로 순회.
        for i, j in y_sizes :
            if i <= x and j <= y :  # 명함 카드가 가로 세로 모두 다 작은면,
                pass                # pass
            else :                  # 그렇지 않으면,
                if i <= y and j <= x :  # 회전시켜서 확인.
                    pass
                else :                  # 회전시켜도 xy가 작으면,
                    y = j if j < i else i   # 세로값을 i,j중에 작은값으로 교체.
    else:
        x = x_sizes[0][0]
        for i, j in x_sizes :
            if i <= x and j <= y :
                pass
            else :
                if i <= y and j <= x :
                    pass
                else :
                    x = i if i < j else j

    print(x, y)
    answer = x*y
    return answer
