# 최대 2명이니까 혼자 타거나 둘이 타거나.
# 최대한 무게를 채워야하므로, 가장 적은 무게와 가장 큰 무게를 같이 태운다.
# 가장 적은 무게와 가장 큰 무게 > limit 이라면 큰 무게 사람 먼저 혼자 태운다.
from collections import deque
def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    boat = 0
    while people :
        if people[0] + people[-1] <= limit and len(people) > 1 :
            people.pop()
            people.popleft()
        else :
            people.popleft()
        boat += 1


    return boat