import sys

N = int(sys.stdin.readline())               # 시간초과로 sys사용
stack =[]
for _ in range(N) :
    stick = int(sys.stdin.readline())
    while stack and stack[-1] <= stick :    # stack top이 stick보다 작거나 같으면 pop
        stack.pop()
    stack.append(stick)                     # 커지면 push

print(len(stack))