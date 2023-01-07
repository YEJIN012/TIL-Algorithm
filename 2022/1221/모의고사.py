def solution(answers):
    answer = []
    ppl = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    N = len(answers)
    ans_cnt = [0, 0, 0]

    for i in range(len(ppl)):
        for j in range(N):
            if answers[j] == ppl[i][j % len(ppl[i])]:
                ans_cnt[i] += 1
    print(ans_cnt)

    m = max(ans_cnt)
    if ans_cnt.count(m) > 1:
        for i in range(len(ppl)):
            if ans_cnt[i] == m:
                answer.append(i + 1)
    else:
        answer = [ans_cnt.index(max(ans_cnt)) + 1]

    return answer