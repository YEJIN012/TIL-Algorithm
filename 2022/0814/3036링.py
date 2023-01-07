N = int(input())
ring = list(map(int,input().split()))

for i in range(1,N) : # 비교해야할 링의 갯수 만큼 시행 및 출력.

    # 주어진 반지름에 대해 최소공배수를 구하면, 이는 각 링이 회전한 링의 둘레 비와 같다.
    # 최대공약수와 최소공배수 구하기
    min_m = 0
    K = ring[i] if ring[i] < ring[0] else ring[0] # 두 개의 자연수 중 작은 값을 기준으로
    for j in range(K, 0, -1) : # 내림차순 검색
        if ring[0] % j == 0 and ring[i] % j == 0 : # 두 개의 자연수 모두 나누어 떨어트리는 값 = 최대공약수
            max_d = j
            min_m = (ring[0] * ring[i]) // max_d # 두 자연수의 곱 = 최대공약수 * 최소공배수
            break


    # 최소공배수를 반지름으로 나누면 회전 수의 비와 같다.
    A = min_m//ring[i]
    B = min_m//ring[0]
    print(f'{A}/{B}')