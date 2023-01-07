bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
answer = 0

t = 1
onbridge = [[truck_weights[0],1]]
onbridge_weight = truck_weights.pop(0)

while len(truck_weights) != 0 or len(onbridge) != 0 :
    t += 1
    for i in onbridge :
        i[1] += 1
    while onbridge :
        if onbridge[0][1] > bridge_length :
            m = onbridge.pop(0)
            onbridge_weight -= m[0]
        else :
            break
    if truck_weights and onbridge_weight + truck_weights[0] <= weight :
        k = truck_weights.pop(0)
        onbridge_weight += k
        onbridge.append([k,1])
answer = t

print(answer)