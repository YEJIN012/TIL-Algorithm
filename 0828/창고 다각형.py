N = int(input())
column = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1, 0, -1) :                    # 위치 순서대로 정렬.
    for j in range(i) :
        if column[j][0] > column[j+1][0] :
            column[j], column[j+1] = column[j+1], column[j]

max_H = 0
max_H_Indx = -1
for i in range(N) :                             # 최대 높이와 그 인덱스
    if max_H < column[i][1] :
        max_H = column[i][1]
        max_H_Indx = i

area = 0                                        # 최대 높이를 기준으로 앞뒤 분리해서 계산.
stack = [column[0]]
for i in range(0, max_H_Indx + 1) :             # 전반부.
    v = stack[-1]
    if v[1] <= column[i][1] :                   # 오목하면 안되므로 스택 top 높이보다는 크거나 같은 기둥만 push
        stack.append((column[i]))
        area += (column[i][0] - v[0]) * v[1]    # 새로 푸쉬된 기둥 이전까지 넓이 +

stack2 = [column[N-1]]
for i in range(N-1, max_H_Indx - 1 , -1):       # 후반부.
    v = stack2[-1]
    if v[1] <= column[i][1]:                    # 오목하면 안되므로 스택 top 높이보다는 크거나 같은 기둥만 push
        stack2.append((column[i]))
        area += (v[0] - column[i][0]) * v[1]    # 새로 푸쉬된 기둥 이전까지 넓이 +

area += column[max_H_Indx][1]                   # 최대 높이 기둥 면적 마지막에 +

print(area)


# 반례
# 4
# 1 6
# 3 6
# 5 6
# 7 7
#
# 답 43
#
# 4
# 1 6
# 3 6
# 5 6
# 7 5
#
# 답 40
#
# 5
# 1 6
# 3 9
# 5 8
# 7 7
# 9 8
#
# 답 69
#
# 4
# 1 3
# 2 2
# 3 3
# 4 3
#
# 답 12
#
# 3
# 0 3
# 1 2
# 2 3
#
# 답 9
#
# 5
# 1 5
# 2 4
# 3 2
# 4 3
# 5 1
#
# 답 16
#
# 3
# 0 3
# 1 4
# 2 3
#
# 답 10
#
# 3
# 1 3
# 2 2
# 3 3
#
# 답 9