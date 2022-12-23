# 순열(DFS)
def npr(i,r) :
    if i == r :
        print(A)
        ans = ''.join(map(str, A))  # 각 순열 결과값(list)을 str로 join
        total_num.append(int(ans))  # 결과값을 int 형태로 전체 숫자 리스트에 push
    else :
        for j in range(N) :
            if used[j] == 0 :
                A.append(numbers_list[j])
                used[j] = 1
                npr(i+1,r)
                A.pop(-1)
                used[j] = 0

# 숫자n 소수판별 : 루트n까지 값으로 나누었을 때, 나누어 떨어지면 소수가 아니다.
def prime(n):
    cnt = 1
    if n == 2 :
        pass
    else :
        for k in range(2, n + 1):
            if k * k <= n:
                if n % k == 0:
                    cnt = 0
                    break
            else:
                break
    return cnt

numbers = "1230"
answer = 0
total_num = []      # 종이조각으로 만들 수 있는 숫자 전체.
numbers_list = []   # 문자열 numbers를 리스트로 변형.
for i in numbers :
    numbers_list.append(int(i))
N = len(numbers_list)

# 가능한 자리수 모두를 순열로 구하기.
for r in range(1, N+1) :
    used = [0] * N
    A  = []                 # 각 순열 결과값
    npr(0,r)
total = set(total_num)      # set -> 중복값 제거
print(total)

for k in total :
    answer += prime(k)
print(answer)

