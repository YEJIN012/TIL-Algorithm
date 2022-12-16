scoville = [1,1,1,1,1,1,100,100,100,100,0,0,0,0,0]
# scoville = [1, 2, 3, 9, 10, 12]
# scoville = [0, 1, 3, 4, 10, 12]
K = 7
answer = 0

# Heap
# 힙에서는 루트 노드의 원소만을 삭제.
#  -> 최소힙 사용.
import heapq
heapq.heapify(scoville)     # heapify -> 최소힙 정렬

while scoville[0] <= K:
    if len(scoville) == 1:
        answer =  -1
        break
    else :
        a=heapq.heappop(scoville)   # heappop -> heap.pop(0) 후에 최소힙 재정렬
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)  # heappush -> heap.append(a+b*2) 후에 최소힙 재정렬
        answer += 1
print(answer)


# 시간 초과
# while scoville and min(scoville) < K :
#     if len(scoville) == 1 :
#         answer = -1
#         break
#
#     else :
#         a = scoville.pop(scoville.index(min(scoville)))
#         b = scoville.pop(scoville.index(min(scoville)))
#         scoville.append(a + b * 2)
#         answer += 1
# print(answer)
