F, S, G, U, D = map(int, input().split())

visited = [0] * (F+1)
q = [S]
visited[S] = 1
possible = False
while q :
    i = q.pop(0)
    if i == G :
        possible = True
        break
    Ui = i + U
    if 0<Ui<=F and visited[Ui] == 0 :
        visited[Ui] = visited[i] + 1
        q.append(Ui)

    Di = i - D
    if 0<Di<=F and visited[Di] == 0 :
        visited[Di] = visited[i] + 1
        q.append(Di)
else :
    print('use the stairs')

if possible :
    print(visited[G]-1)