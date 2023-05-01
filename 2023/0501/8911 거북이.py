rotate = [(0,1),(1,0),(0,-1),(-1,0)]
N = int(input())
for _ in range(N) :
    route = input()
    k = 0           # 방향 전환 -> rotate배열 index
    now = (0,0)     # 현재 위치
    # X좌표 최대최소의 차와 Y좌표 최대최소의 차의 곱으로 직사각형 넓이를 구하기 위해
    # 구분해서 배열에 저장.
    X=[0]
    Y=[0]
    for i in range(len(route)) :
        # 명령 네가지 조건에 따른 위치변환
        if route[i] == 'F' or route[i] == 'B' :
            if route[i] == 'F' :
                now = (now[0] + rotate[k][0], now[1] + rotate[k][1])
            elif route[i] == 'B' :
                now = (now[0] - rotate[k][0], now[1] - rotate[k][1])
            X.append(now[0])
            Y.append(now[1])
        elif route[i] == 'L' or route[i] == 'R' :
            if route[i] == 'L' :
                k = (k+1)%4
            elif route[i] =='R' :
                k = (k-1)%4
    print((max(X)-min(X)) * (max(Y)-min(Y)))