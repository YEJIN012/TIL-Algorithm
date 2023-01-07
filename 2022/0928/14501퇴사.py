# DP
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
baekjun = [0] * (N+1)                    # 백준이의 스케쥴별 수익 합산(역순) -> 최초 i+1 인덱스연산을 위해. N+1 크기로 제작. baekjun[N+1] = 0

for i in range(N-1, -1, -1) :       # 마지막 날부터 역순으로 스케줄 확정.
    if i + schedule[i][0] > N :    # 일정이 퇴사일을 넘어가는경우,
        baekjun[i] = baekjun[i+1]   # 이전까지 존재하는 합산 그대로 받는다. ex) 마지막 3일이 [[4,40],[2,200],[1,100]] 인 경우, 마지막날 100을 앞에도 복사해놔야 합산/비교가능..
    else :                          # 넘어가지 않는 날짜부터, 비교 시작.
        baekjun[i] = max(baekjun[i+1], baekjun[i+schedule[i][0]] + schedule[i][1])
        # i일의 스케줄을 포함하지않은 경우(i+1일의 합산금액)
        # vs i일의 스케줄을 포함하는 경우
        # (i일 스케줄 상담기간만큼 뒤로간 날짜의 합산금액 + i일의 스케줄을 포함한(i일 스케줄의 수익))
        # 중 큰 수익금액.
print(baekjun[0])