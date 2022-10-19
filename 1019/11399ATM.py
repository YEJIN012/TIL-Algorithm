N = int(input())
time = list(map(int, input().split()))
time.sort()
k = time[0]
wait = k
for n in range(1,N) :
    k += time[n]
    wait += k

print(wait)
