import sys
sys.setrecursionlimit(50*50)

def dfs1(i, j) :
    design[i][j] = 0        # 인접한 같은 모양은 하나의 판자이므로, 카운트 했음을 0으로 표시.
    if 0<=j+1<M and design[i][j+1] == '-' :
        dfs1(i, j+1)
def dfs2(i, j) :
    design[i][j] = 0
    if 0<=i+1<N and design[i+1][j] == '|' :
        dfs2(i+1, j)



N, M = map(int, input().split())
design = [list(input()) for _ in range(N)]
cnt = 0                             # 필요한 나무판자의 수

for i in range(N) :                 # design 행렬 전체순회.
    for j in range(M) :
        if design[i][j] == '-' :    # 새로운 '-' 모양이 등장하면,
            cnt += 1                # 나무판자 +1
            dfs1(i, j)              # 연속된 '-' 모양 탐색 함수 실행
        elif  design[i][j] == '|' : # 새로운 '|' 모양이 등장하면,
            cnt += 1                # 나무판자 +1
            dfs2(i, j)              # 연속된 '|' 모양 탐색 함수 실행
print(cnt)