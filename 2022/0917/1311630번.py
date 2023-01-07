import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1 ) :
    A, B = map(int, input().split())
    # a, b = A, B if A < B else B, A
    if A < B :
        a, b = A, B
    else :
        a, b = B, A

    while b != a  :
        if b > a :
            b = b // 2

        elif a > b :
            a = a // 2

    if b == a:
        print(b * 10)