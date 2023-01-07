A, B = map(int,input().split())
arr = []
k = 1
s = 1
ans = 0
for i in range(A, B+1) :
    while k < i :
        s += 1      # 1을  , 2를 , 3을
        k += s      # 한 번, 두 번, 세 번
    ans += s
print(ans)