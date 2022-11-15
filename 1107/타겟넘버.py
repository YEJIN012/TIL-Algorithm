# 모든 경우의 수를 다 세야겠다고 생각하게 되었는데,
# 가장 간단한 경우부터 생각해 보았어요.
# 숫자가 하나만 있을 경우에는 하나만 더하거나 빼서 두가지경우가 나올 것이고
# 두개가 있을경우에는 앞숫자 결과에서 또 두가지로 분기가 될것이라고 생각했습니다.
# 그래서 이런식으로 분기를 나눠가면서 모든 경우를 찾아보려면 bfs나 dfs를 사용하면 되겠다고 생각했고,
# 어차피 최종 레벨은 같을것이기 때문에 bfs로 선택했습니다.
# 각각의 합은 큐에 함께 넣어서 번거로움을 줄이고 싶었고
# 이런 생각은 bfs나 dfs 문제 자주풀면 반복되는거라서 기계적으로 풀었던것같습니다.

# bfs
def solution(numbers, target):
    answer = 0
    q = [(0, 0)] # sum, n
    while q:
        sum, n = q.pop(0)

        if n > len(numbers):
            break
        elif n == len(numbers) and sum == target:
            answer += 1
        q.append((sum+numbers[n-1], n+1))
        q.append((sum-numbers[n-1], n+1))

    return answer