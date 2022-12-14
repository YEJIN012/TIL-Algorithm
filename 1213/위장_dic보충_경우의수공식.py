clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

answer = 0
dic = {}
for x,y in clothes :
    if y in dic :
        dic[y].append(x)
    else :
        dic[y] = [x]    # value값을 다중으로 받으려면, 처음 생성부터 value를 리스트로 만들어줘야 한다.
# print(dic)            # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}

# 그냥 부분집합 갯수 구하는 공식만 있으면 됨...
# {a, b, c, d} 의 부분집합은 a있고 없고, b가 있고 없고 ... 의 순열로 2^4 승이다.
# 같은 식으로 이 문제에서는
# headgear 가 없거나 'yellow_hat' 이거나, 'green_turban'이거나 와 eyewear가 없거나 'blue_sunglasses' 이거나 의 순열이다.
# 하지만 하나 이상은 무조건 착용해야하므로 모두 없거나에 해당되는 경우의 수 1을 빼줘야 한다.
# 즉, (2+1)*(1+1)-1 = 3*2-1 = 5
answer = 1
for i in dic.values() :
    answer *= (len(i)+1)
answer -= 1
print(answer)


### 다른사람 답
# def solution(clothes):
#     clothes_type = {}
#
#   len안도록 처음부터 카운트 딕셔너리
#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2       # 없는 경우도 있어야하므로 미리 +1 한 2를 value로 딕셔너리 생성.
#         else:
#             clothes_type[t] += 1
#
#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num
#
#     return cnt - 1


### dictionary는 비시퀀스형 자료이므로 index가 없다. 부분집합 목록 구하는 공식 불가능.
# N = len(dic)
# k = 0
# for i in range(1,1<<N) :
#     p = 1
#     for j in range(N) :     # j 는 원소리스트 각각의 index
#         if i & (1 << j):
#             print(dic[j])
#             p *= len(dic[j])
#     k += p
# print(k)

