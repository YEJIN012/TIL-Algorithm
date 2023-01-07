N = str(input())
cnt = [0] * 9                   # 방번호 카운트배열
for i in range(len(N)) :
    if N[i] == '9' :            # 방번호가 9일때는 6으로 카운트
        cnt[6] += 1
    else :
        cnt[int(N[i])] += 1
cnt[6] = -((-cnt[6]) // 2)      # 6,9 모두 카운트 되었으므로 // 2 (음수 나눗셈의 몫 -> 올림)
print(max(cnt))