# def npn(i, C) :
#     global ans
#     if i == N :
#         if C[0] != '0':             # 0으로 시작하지 않는 C
#             if int(C) < int(B) :    # B보다 작으면
#                 if ans == 0 :       # 정답을 못찾았을 때만
#                     ans = 1         # 정답 찾았다고 표시하고
#                     print(C)        # 출력.
#                 else :
#                     return
#
#     else :
#         for j in range(N-1,-1,-1) : # 내림차순 순열
#             if used[j] == 0 :
#                 used[j] = 1
#                 npn(i+1, C + A[j])
#                 used[j] = 0
#
# A, B = input().split()
# A = sorted(A)                       # used를 활용한 내림차순 순열함수를 사용하기 위해서는 주어지는 원소리스트가 오름차순이어야한다.
# N = len(A)
# ans = 0
# used = [0] * N
# npn(0, '')
# if ans == 0 :                       # 순열을 다 만들고 나서도 답이 없으면,
#     print(-1)                       # -1 출력.


def npn(i, C) :
    global ans
    if i == N :
        if C[0] != '0':             # 0으로 시작하지 않는 C
            if int(C) < int(B) :    # B보다 작으면
                if ans == 0 :       # 정답을 못찾았을 때만
                    ans = 1         # 정답 찾았다고 표시하고
                    print(C)        # 출력.
                else :
                    return

    else :
        for j in range(N) : # 내림차순 순열
            if used[j] == 0 :
                used[j] = 1
                npn(i+1, C + A[j])
                used[j] = 0

A, B = input().split()
A = sorted(A, reverse=True)                       # used를 활용한 내림차순 순열함수를 사용하기 위해서는 주어지는 원소리스트가 오름차순이어야한다.
N = len(A)
ans = 0
used = [0] * N
npn(0, '')
if ans == 0 :                       # 순열을 다 만들고 나서도 답이 없으면,
    print(-1)                       # -1 출력.
