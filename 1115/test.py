ss = [12,43,4,2,6,10,7,4,8,898,34]
N = len(ss)

for i in range(N-1,0,-1):
    for j in range(0, i):
        if ss[j] > ss[j + 1]:
            ss[j], ss[j + 1] = ss[j + 1], ss[j]
            print(ss)

print(ss)

# s=['3', '4']
# print(s[0]+s[0])