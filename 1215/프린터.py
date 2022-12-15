priorities = [1,3,4,7,5,3,6,7,9,2]
location = 2
answer = 0

# priorities 의 인덱스 -> 출력물의 고유번호이자, 요청순서
p = priorities.index(max(priorities))   # 첫번째 프린트 (p : 현재 출력물)
# print(p)
cnt = 1     # 프린트 순서
if p != location :
    while priorities :
        if p != len(priorities)-1 :     # 출력물이 목록에서 마지막에 놓여있지 않으면,
            l = priorities[p+1:]        # 현재 프린트 된 문서 뒤에 놓인 작업물 리스트
            priorities[p] = -1          # 출력완료 표시.(작업물들의 고유index가 바뀌면 안되므로, pop은 지양.)
            if max(priorities) > max(l) :   # 현재 출력 된 문서 뒷 순서에 놓인 문서리스트에서의 최대중요도보다 대기목록(현재 출력 된 작업물보다 앞 index)의 최대중요도가 클 때,
                p = priorities.index(max(priorities))   # 전체 작업물리스트에서의 최대중요도 작업물 프린트 -> 전체 작업물리스트 = 대기목록
            else :                              # 아니면,
                p = l.index(max(l)) + p + 1     # 뒤에 놓인 작업물 리스트에서의 최대중요도 작업물 프린트
        else :                          # 출력물이 목록에서 마지막에 놓여있지 있으면, (위에 비교들을 할 필요가 없음. l이 없기 때문에)
            priorities[p] = -1
            p = priorities.index(max(priorities))
        # print(p)
        cnt += 1                        # 프린트 순서 +1
        # print(priorities)
        if p == location :              # 출력물이 내가 요청한 문서일 때,
            break                       # 중단.
answer = cnt
print(answer)
# 6



# 다른사람 코드
# any 함수
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer
