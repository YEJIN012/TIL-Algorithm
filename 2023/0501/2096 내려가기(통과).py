N = int(input())

min_list = [0,0,0]  # 현재 행(최소)
max_list = [0,0,0]  # 현재 행(최대)
for i in range(N) :
    row = list(map(int, input().split(' ')))    # 내려갈 다음 행
    # 다음 행에서의 각 칸을 기준으로(역순)
    # 각 칸으로 이동가능한 칸 중 최소/최대를 즉시 구해 해당 값과 의 합으로 현재 행(내려온 행)을 갱신한다.
    min_list = [row[0]+min(min_list[0],min_list[1]), row[1]+min(min_list[0], min_list[1], min_list[2]), row[2]+min(min_list[1], min_list[2])]
    max_list = [row[0]+max(max_list[0],max_list[1]), row[1]+max(max_list[0],max_list[1],max_list[2]), row[2]+max(max_list[1], max_list[2])]

print(max(max_list),min(min_list))
