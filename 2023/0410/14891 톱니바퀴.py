arr =[list(map(str,input())) for _ in range(4)]
K = int(input())

for _ in range(K) :
    R = [0] * 4     # 하나의 톱니바퀴 회전에 의해 결정되는 전체 톱니바퀴의 방향
    k, rotate = map(int, input().split())
    k -= 1  # index 맞춤
    R[k] = rotate

    # k와 k의 회전방향을 기준으로
    k_right = k
    r_right = rotate
    # 오른쪽에 있는 톱니와 비교
    while k_right < 3 :
        if r_right != 0 :
            # index 2 톱니와 index 6 톱니 비교
            # 서로 다른 극이면,
            if arr[k_right][2] != arr[k_right+1][6] :
                r_right = -1 * r_right  # 반대로 회전
                R[k_right+1] = r_right
            # 서로 같은 극이면,
            else :
                r_right = 0     # 정지
            k_right += 1
        # 동일한 방향에 톱니바퀴 모두 정지.
        else :
            break

    # k와 k의 회전방향을 기준으로
    k_left = k
    r_left = rotate
    # 왼쪽에 있는 톱니와 비교
    while k_left > 0 :
        if r_left != 0 :
            # index 6 톱니와 index 2 톱니 비교
            # 서로 다른 극이면,
            if arr[k_left][6] != arr[k_left-1][2] :
                r_left = -1 * r_left    # 반대로 회전
                R[k_left-1] = r_left
            # 서로 같은 극이면,
            else :
                r_left = 0      # 정지
            k_left -= 1
        # 동일한 방향에 톱니바퀴 모두 정지.
        else :
            break

    # 방향에 맞춰 톱니별로 한칸씩 이동
    for i in range(4) :
        # 시계방향
        if R[i] == 1 :
            # index 7 부터 역순으로 복사이동해야함.
            tmp1 = arr[i][0]
            for j in range(7,0,-1) :
                arr[i][(j + 1) % 8] = arr[i][j]
            arr[i][1] = tmp1
        # 반시계방향
        elif R[i] == -1 :
            tmp2 = arr[i][7]
            for j in range(0, 7):
                arr[i][(j - 1) % 8] = arr[i][j]
            arr[i][6] = tmp2

ans = 0
for i in range(4) :
    if arr[i][0] == '1' :
        ans += 2**int(i)

print(ans)