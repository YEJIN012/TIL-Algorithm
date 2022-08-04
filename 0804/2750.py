#### input 여러줄 받는 다른방법 ####
# N = int(input())
# numbers = list(input() for _ in range(N))
# # input() for _ in range(n)n개의 줄 입력 받기 #
# # numbers = N개줄의 입력을 받아 list화 한다.
# # 왜때문인지 numbers = list(map(int,input() for _ in range(N))) 으로 한번에 묶이지는 않는다..
# numbers = list(map(int,numbers))
# # str 타입으로 들어간 요소들을 map을 사용하여 int 형식으로 바꿔서 재리스트화

# numbers.sort() # 오름차순으로 정렬. type = list

# for i in numbers :
#     print(i) # 정렬된 요소들을 list에서 차례로 꺼내 한줄씩 출력.

N = int(input())
numbers = [] # 빈 리스트를 먼저 만든다.
for i in range(N): 
    numbers.append(int(input())) # for 문과 함께 N개의 input값을 int형식으로 빈 리스트에 담는다.
numbers.sort() # 오름차순으로 정렬. type = list
for i in numbers:
    print(i) # 정렬된 요소들을 list에서 차례로 꺼내 한줄씩 출력.