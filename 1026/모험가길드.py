# 공포도가 낮은 사람부터 순서대로 최소한의 인원으로 그룹생성.
N = int(input())
ppl = list(map(int, input().split()))
ppl.sort()
cnt = 0
members = 0
for i in ppl :
    members += 1
    if i <= members :
        cnt += 1
        members = 0

print(cnt)

# # !! 안되는 코드 !!
# # 공포도가 큰 사람 순서대로 최소한의 인원으로 그룹 생성.
# # -> 남는 인원 있으면 안되는 줄,,,
# N = int(input())
# ppl = list(map(int, input().split()))
# ppl.sort(reverse=True)
# cnt = 0
# i = 0
# while i < len(ppl) :
#     i += ppl[i]
#     cnt += 1
# print(cnt)
#
# # 반례 :
# # 1 1 1 2 2 3 5
# # 정답 : 3
# # 오답 : 4