array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
array = [0]+array
answer = [0]*len(commands)
for i in range(len(commands)) :
    a = [0] + array[commands[i][0]:commands[i][1]+1]
    a.sort()
    answer[i] = a[commands[i][2]]
print(answer)
