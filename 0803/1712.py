A, B, C = map(int,input().split())
# print(A, B, C) # <class 'int'>
if C > B :
    point = A // (C-B) +1
    if point <= 0 :
        point = -1
else :
    point = -1
print(point)

# import math

# A, B, C = map(int,input().split())
# # print(A, B, C) # <class 'int'>
# if C > B :
#     point = A / (C-B)
#     point = math.trunc(point) + 1
#     if point <= 0 :
#         point = -1
# else :
#     point = -1
# print(point)