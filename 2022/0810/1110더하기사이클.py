N = int(input())
cnt = 0
new_N = -1 # 입력값이 0이상이므로 new_N을 -1로 시작.
p_N = N # 초기입력값을 변수 p_N(previous_N)으로 설정하고 시작.
p_N_10 = 0 # 10보다 작은 수를 고려하여 필요함.

# 초기 입력값 N은 절대 변하지 않는다.
while new_N != N :
    if p_N < 10:
        p_N_10 = p_N * 10
    else:
        p_N_10 = p_N
    new_N = ((p_N % 10) * 10) + (((p_N_10 // 10) + (p_N_10 % 10)) % 10)
    cnt += 1 # 사이클 카운팅
    p_N = new_N # 새로운 수를 이전 수로 변경.

print(cnt)