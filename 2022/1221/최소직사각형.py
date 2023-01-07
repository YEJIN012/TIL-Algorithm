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

# # 다른사람 풀이
# # sizes = [[3,5],[6,2]]
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# print(list(max(x) for x in sizes))
# print(list(min(x) for x in sizes))
# print(max(max(x) for x in sizes) * max(min(x) for x in sizes))
#
# # 다른사람 풀이2
#
# print(list(sum(sizes, [])))     # sum의 두번째 인자(start)에 empty list를 전달해서 sizes의 총합이 아니라 sizes의 모든 요소가 담긴 1차원 list로 변환
#                                 # start = [] , 빈배열 start에 size 리스트를 계속 더해준다.
# # [60, 50, 30, 70, 60, 30, 80, 40]
# # max(sum(sizes, [])) 항상 같음 -> 80
#
# solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
# print(solution(sizes))

