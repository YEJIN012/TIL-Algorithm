arr = [[0,0,0,0],[0,2,1,0],[0,1,2,0],[0,0,0,0]]
N, M = map(int,input().split())
for _ in range(M):
    a, b, s = map(int, input().split())
    j = a - 1
    i = b - 1

    arr[i][j] = s
    k = 1

    for di, dj in [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]:  # 가로,세로,대각선 모두 검사.
        change = []
        while 0 <= i + k * di < N and 0 <= j + k * dj < N and arr[i + k * di][j + k * dj] != 0 and arr[i + k * di][j + k * dj] != arr[i][j]:  # 인접칸이 범위 이내이고, 현재 칸과 다른 색이 올려져있으면,
            if 0 <= i + (k + 1) * di < N and 0 <= j + (k + 1) * dj < N and arr[i + (k + 1) * di][j + (k + 1) * dj] != 0 and arr[i + (k + 1) * di][j + (k + 1) * dj] != arr[i][j]:  # 그 다음칸 확인. 그 다음칸도 현재 칸과 다른 색 돌이면,
                change.append((i + k * di, j + k * dj))  # 담는다.
                k += 1  # 옆 인접칸 계속 검토.
            elif 0 <= i + (k + 1) * di < N and 0 <= j + (k + 1) * dj < N and arr[i + (k + 1) * di][j + (k + 1) * dj] != 0 and arr[i + (k + 1) * di][j + (k + 1) * dj] == arr[i][j]:  # 다음칸이 현재 칸과 같은 색이면,
                change.append((i + k * di, j + k * dj))  # 담는다.
                for ni, nj in change:  # 담겨진 돌은 다 내꺼.
                    arr[ni][nj] = arr[i][j]
                k = 1
                break
            else:
                k = 1
                break

