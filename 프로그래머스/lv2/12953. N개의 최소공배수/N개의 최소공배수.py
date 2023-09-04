# 최소공배수 공식 : 최소공배수 = (x*y) / x,y의 최대공약수
def solution(arr):
    from math import gcd    # 최대공약수 구하는 함수
    answer = arr[0]                                 # answer을 arr[0]으로 초기화

    for i in arr:
        # 주어진 숫자 배열을 돌면서 모두의 최소공배수를 누적하여 구한다.
        # ex. a,b,c,d -> a와 b의 최소공배수와 그 수와 c의 최소공배수와 그 수와 d의 최소공배수
        answer = answer*i // gcd(answer, i)     

    return answer

