# 단어a와 단어b 사이 다른 알파벳의 갯수 찾는 함수
def diff(a, b, n):
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
    return cnt

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
def solution(begin, target, words):
    answer = 0
    words = [begin] + words                 # words리스트 index 0에 begin 단어 추가
    N = len(words)
    n = len(begin)

    # 그래프 생성
    graph = list([] for _ in range(N))      # 알파벳 하나만 다른 단어와 단어의 graph (인자 -> words index)
                                            # 한번에 한개의 알파벳을 바꿀 때 이동가능한 word 그래프
    for i in range(N):
        for j in range(N):
            if i != j:
                if diff(words[i], words[j], n) == 1:    # 단어a와 단어b 사이 다른 알파벳의 갯수가 하나이면,
                    graph[i].append(j)                  # graph 연결.
    print(words)
    print(graph)
    # ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
    # [[1], [0, 2, 4], [1, 3, 4], [2, 5, 6], [1, 2, 5], [3, 4, 6], [3, 5]]

    if target in words:     # target 문자로 변환이 가능하면,
        # bfs
        visited = [0] * N
        q = [0]
        visited[0] = 1
        while q:
            i = q.pop(0)
            if words[i] == target:
                answer = visited[i] - 1 # 시작 문자(begin)을 1로 시작했으므로, 단계 횟수는 visited-1
                break
            for di in graph[i]:     # graph[i] : words[i] 문자가 한개의 알파벳을 바꿀때에 나타날 수 있는 문자(words index) 후보군.
                if visited[di] == 0:
                    visited[di] = visited[i] + 1
                    q.append(di)
        print(visited)

    return answer