def dfs(a, b) :
    # global cnt
    visited[a] = 1
    while True:
        if a == b:                      # b에 도달했으면 촌수 출력, 탐색종료.
            print(len(stack))           # 촌수 = stack에 남아있는 수와 동일
            # print(cnt)                # 별도 촌수 카운트 필요없음!
            break
        else:
            for i in tree[a]:
                if visited[i] == 0:     # 방문하지 않은 인접점이 있으면,
                    stack.append(a)     # 이미 방문한 a를 push
                    # cnt += 1
                    a = i               # 방문할 i 를 현재 위치로
                    visited[i] = 1      # 방문 표시
                    break

            else:                       # 방문하지 않은 인접점이 없고
                if stack:               # 스택이 비어있지 않으면,
                    a = stack.pop()     # 스택 top을 pop하고 그곳에서 다시 탐색
                    # cnt -= 1
                else :                  # 스택이 비어있으면,
                    print(-1)           # 촌수 계산 불가.
                    break



n = int(input())
a, b = map(int, input().split())
m = int(input())
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m) :
    x, y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
# print(tree)
stack = []
# cnt = 0
dfs(a, b)


# 9
# 8 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]