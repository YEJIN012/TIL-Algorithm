import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
arr = [0] * (N+1)
for _ in range(Q) :
    land = int(input())    # 원하는 땅
    first = 0              # 점유된 땅 (while문을 다 돌고나면 처음 마주치는 점유된 땅)
    now = land
    while now != 1 :       # 원하는 땅에서부터 1까지 이동.
        if arr[now] == 1 : # 점유된 땅이 발견되면 저장.
            first = now
        now = now // 2
    if first == 0 :        # 처음 마주치는 점유된 땅이 0 이면
        arr[land] = 1      # 원하는 땅을 점유할 수 있다는 것이므로 1로 점유 표시.

    print(first)