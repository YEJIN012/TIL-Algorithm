N = int(input())

if N % 5 == 0 :
    cnt1 = N // 5

elif N % 3 == 0 :
    cnt1 = N // 3

else : # 5 또는 3으로 나누어 떨어지지 않는 경우,
    cnt1 = 5000 # 마지막에 cnt1 값이 출력되지 않도록 최대값을 부여.




### 5키로와 3키로를 함께 써서 최소값을 구할 수 있는 경우 ###

i = N // 5  # i를 큰 값에서부터 확인해야 cnt2가 가장 작은 경우의 수가 나옴.
# ex)
# i = 1
# while 5 * 1 < N :
#     .
#     .
#     .
#     i += 1
# 로 돌리면 [Hidden case] N = 4003 일 때, 1333이 나옴.
while i > 0 :
    if (N - 5 * i) % 3 == 0 :
        cnt2 = i + (N - 5 *i) // 3
        break
    else :
        i -= 1

else : # 5와 3으로 나누어 떨어지지 않을 때,
    if cnt1 == 5000 : # cnt1 값도 없으면,
        cnt2 = -1 # N킬로그램 만들 수 없음. -1 출력.
    else :
        cnt2 = 5000 # cnt1값이 있으면, cnt2값이 출력되지 않도록 최대값 부여.



print(cnt1 if cnt1 < cnt2 else cnt2) # cnt1 과 cnt2 중 작은 값 출력.