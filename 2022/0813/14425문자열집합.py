N, M = map(int,input().split())
N_words = list(input() for _ in range(N))
M_words = list(input() for _ in range(M))

cnt = 0
for m in M_words : # 입력받은 M개의 문자들이
    if m in N_words  : # 집합 S에 포합되어 있으면,
        cnt += 1 # 카운트.

print(cnt)