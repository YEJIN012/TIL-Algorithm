N_str = input() # 처음 주어진 값을 문자열 그대로 받는다. 자릿수를 알기 위해.
N = int(N_str) # 문자열로 받은 입력값을 다시 숫자로 반환.
cnt = 0 # 새로운 수의 자릿수 세팅

# 새로이 작성되는 숫자가 1부터 주어진 숫자까지 이므로,
# 각 자릿수 별로 패턴을 확인해 보자면,

# N이 4자리 수 이면, 새로이 작성되는 수로 작성되는 수들은
# 1~9(9개), 10 ~ 99(90개), 100 ~ 999(900개), 1000 ~ N(N - 1000 + 1 개) 이다.
# 해당 갯수들에 자릿수를 곱한 값의 합이 새로운 수의 자리 수 이다.


k = 9

for i in range(1,len(N_str)) : # 한자리 수 부터 입력값 N의 자리수 -1 까지 계산.
    cnt += k * i
    k *= 10

# 마지막 len(N_str)자리수까지 계산.
cnt += (N - (10 ** (len(N_str)-1)) + 1) * len(N_str)

print(cnt)