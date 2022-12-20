operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
answer = []
import heapq
q = []
while operations :
    tmp = operations.pop(0)
    if tmp[0] == 'I' :
        num = int(tmp[2:])
        heapq.heappush(q, num)
    else :
        if q :
            if tmp == 'D -1' :
                heapq.heappop(q)
            else :
                q.pop(q.index(max(q)))
                heapq.heapify(q)

if q :
    answer = [max(q), q[0]]
else :
    answer = [0,0]
print(answer)