# N = int(input())
# arr = [[0] * 100 for _ in range(100)]
# area = 0
# for _ in range(N) :
#     j, i = map(int, input().split())
#     for k in range(10) :
#         for l in range(10) :
#             if arr[99-i-k][j+l] == 0 :
#                 arr[99-i-k][j+l] = 1
#                 area += 1
# print(area)


N = int(input())
arr = [[0] * 100 for _ in range(100)]
area = 0
for _ in range(N) :
    j, i = map(int, input().split())
    for k in range(10) :
        for l in range(10) :
            if arr[i+k][j+l] == 0 :         # (좌표->행렬) 상하 반전되어도 상관 없음.
                arr[i+k][j+l] = 1
                area += 1
print(area)
