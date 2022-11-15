# 첫번째 등장한 숫자의 반대를 찾아서 뒤집으면 됨.

N = input()
N += N[0]
cnt = 0
i = 0
while i < len(N):
    if N[i] == N[0] :
        i += 1
    else :
        while N[i] != N[0] :
            i += 1
        else :
            cnt += 1
            i += 1
print(cnt)