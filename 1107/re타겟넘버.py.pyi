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