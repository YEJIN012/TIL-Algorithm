H, W = map(int, input().split())
blocks = list(map(int,input().split()))

ans = 0

# 해당칸별로 고일 수 있는 빗물의 양을 더해준다.
# 현재 블록을 기준으로 양쪽 어딘가 현재보다 높은 블록이 없다면 해당 블록에는 빗물이 고일 수 없음. (처음과 끝 블록은 제외)

for i in range(1, W-1) :
    # 왼쪽 오른쪽 각각 최대 높이 블록을 선택
    left = max(blocks[:i])
    right = max(blocks[i+1:])

    if left > blocks[i] and right > blocks[i] : # 현재 블록보다 높은 블록이 양쪽 모두 있다면,
        ans += min(left, right) - blocks[i]   # 둘 중에 낮은 블록을 기준으로 고일 수 있음.

print(ans)