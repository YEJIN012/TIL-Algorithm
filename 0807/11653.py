N = int(input())
p = 2
# 나누는 수 p를 첫번째 소수인 2로 설정.
while N != 1 :
# while문으로 N=1일 때는 반복문을 빠져나와 아무 출력이 안되도록 설정.
    if N % p == 0 :
    # 입력값 N을 p 나눌 때 나머지가 0이면 
        N = N / p
        # p 로 나눈 값의 몫을 N이라고 가지고 다시 while문 반복. N=1 될때까지.
        print(p)

    else :
        p += 1
        # 나누어 떨어지지 않으면 p값을 키워가며 나머지가 0이 되는 소수p값을 찾는다.
        # p 값을 가장 작은 소수 2부터 설정하여 키워가기 때문에 p는 소수가 나올 수 밖에 없다.