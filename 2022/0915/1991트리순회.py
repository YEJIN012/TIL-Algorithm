def preorder(n) :
    if node[n] :
        print(node[n], end='')
        preorder(node.index(ch1[n]))        # 자식배열에 들어있는 알파벳을 node에서 찾아 그자리의 인덱스를 그다음 n으로 삼는다.
        preorder(node.index(ch2[n]))
def inorder(n) :
    if node[n]:
        inorder(node.index(ch1[n]))
        print(node[n], end='')
        inorder(node.index(ch2[n]))
def postorder(n) :
    if node[n]:
        postorder(node.index(ch1[n]))
        postorder(node.index(ch2[n]))
        print(node[n], end='')

N = int(input())
node = [0] * (N+1)
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
for i in range(1,N+1) :             # 입력값을 처례대로 받고, node의 인덱스와 ch1과 ch2의 인덱스로 엮어준다.
    info = list(input().split())
    node[i] = info[0]
    if info[1] != '.' :
        ch1[i] = info[1]
    if info[2] != '.' :
        ch2[i] = info[2]
preorder(1)
print()
inorder(1)
print()
postorder(1)
