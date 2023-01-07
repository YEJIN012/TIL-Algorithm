import sys
sys.setrecursionlimit(100000)   # 10000은 런타임에러

def pre(left, right) :
    if left > right :
        return
    else :
        mid = right + 1
        for i in range(left + 1, right + 1) :
            if tree[i] > tree[left] :
                mid = i
                break

        pre(left+1, mid-1)
        pre(mid, right)
        print(tree[left])



tree = []
# 입력값 개수가 지정되지 않았으므로, try/except 반복문을 통해 입력값이 없어서 에러가 나올 때까지 반복하여 입력값을 받도록 설정.
while True :
    try :
        tree.append(int(sys.stdin.readline()))
    except :        # ZeroDivisionError, AttributeError, NameError, TypeError 등 어떠한 에러든 모두 예외입니다.
        break
# print(tree)

pre(0, len(tree)-1)




# ch1, ch2 만들어서 후위순회하는거.......fail
# ch1 = [0] * (10**6 + 1)
# ch2 = [0] * (10**6 + 1)
#
# stack = []
# for i in range(N) :             # 주어진 전위순회 결과를 통해 부모인덱스를 한 자식노드 리스트 만들기.
#     if i+1 < N :
#         if tree[i] > tree[i+1] :        # 다음값이 더 작으면, 왼쪽 서브트리이므로
#             stack.append(tree[i])       # 현재 노드를 stack에 저장 후, (왼쪽 서브트리가 있을 때만, 부모가 stack에 담김.)
#             ch1[tree[i]] = tree[i+1]    # 현재 노드를 부모 노드로, 다음 값을 왼쪽 자식노드로 저장.
#         else :                          # 다음 값이 더 크면, 오른쪽 서브트리이므로,
#             if stack[-1] < tree[i + 1]: # stack값이 다음값보다 작으면, 부모노드.
#                 k = stack.pop()         # 스택에서 부모노드를 pop
#                 ch2[k] = tree[i + 1]    # 오른쪽 자식노드로 다음값을 저장.
#             else:                       # stack값이 다음값보다 크면, 부모노드가 아님.(왼쪽 서브트리 없이 오른쪽만 있는 경우)
#                 ch2[tree[i]] = tree[i + 1]  # 현재 노드가 부모노드가 됨.

# def pre(n) :
#     if ch1[n] :
#         pre(ch1[n])
#     if ch2[n] :
#         pre(ch2[n])
#     print(n)

# pre(tree[0])