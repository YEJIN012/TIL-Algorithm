# 조건1) 많이 재생된 장르 먼저
# 조건2) 장르 내에서도 많이 재생된 노래 먼저
# 조건3) 장르 내에서 재생횟수가 같으면 고유번호가 낮은 노래 먼저
# 조건4) 장르에 속한 곡이 하나라면, 하나의 곡만 선택
# 베스트 앨범의 고유번호 리스트 return

answer = []
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

### 먼저 조건1을 위해, 전체 장르를 장르별 재생수를 순서대로 정렬한다.
plays_by_genres = {}    # 장르별 재생수 sum 딕셔너리
N = len(genres)         # N = 전체 곡수
for x in range(N) :
    if genres[x] not in plays_by_genres :
        plays_by_genres[genres[x]] = plays[x]
    else :
        plays_by_genres[genres[x]] += plays[x]
# print(plays_by_genres)        # {'classic': 1450, 'pop': 3100}
genres_order = sorted(plays_by_genres.items(), key = lambda x : x[1], reverse=True)     # 장르별 재생수 기준 정렬 -> for 조건1
# print(genres_order)         #[('pop', 3100), ('classic', 1450)]

### 조건2를 위해, 각 장르에 재생수 높은 애들을 담아주기 위해 곡별 재생수를 순서대로 정렬한다.
songs = {x : plays[x] for x in range(N)}        # 곡별 재생수 기준으로 정렬
songs_order = sorted(songs.items(), key = lambda x : x[1], reverse=True)    # 재생수 기준으로 정렬 -> for 조건2
# print(songs_order)            #[(4, 2500), (3, 800), (1, 600), (0, 500), (2, 150)]

### 장르 순서를 기준으로 실릴 빈 베스트앨범 딕셔너리 생성.
bestalbum = {}       # 장르별 재생수 순서로 실릴 빈 베스트앨범 딕셔너리
for i in range(len(genres_order)) :
    bestalbum[genres_order[i][0]] = []
# print(bestalbum)         # {'pop': [], 'classic': []}

### 조건4를 위해, 베스트앨범에 실릴 최종 수록곡 수 구하기.
nums_by_genres = {x:genres.count(x) for x in genres}    # 베스트앨범 총 수록수를 구하기위해 장르별 곡수 count -> for 조건4
# print(nums_by_genres)           # {'classic': 3, 'pop': 2}
bestalbum_N = 0     # 베스트앨범 총 수록수
for i in nums_by_genres.values() :
    if i >= 2 :
        bestalbum_N += 2
    else :
        bestalbum_N += 1

### 베스트앨범에 실리는 총 곡수 만큼 곡별 재생수 리스트에서 높은 애들을 담아준다.
cnt = 0
for i in range(N) :
    if len(bestalbum[genres[songs_order[i][0]]]) < 2 :      # 곡별 재생수 리스트를 순서대로 순회하며 해당 곡의 장르가 아직 2곡보다 적게 담겨있으면,
       bestalbum[genres[songs_order[i][0]]].append(songs_order[i][0])   # bestalbum에 추가.
       cnt += 1                 # 수록된 곡수 +1
    if cnt == bestalbum_N :     # 수록된 곡수가 베스트앨범 총 수록수과 같아지면 stop
        break
# print(bestalbum)     # {'pop': [4, 1], 'classic': [3, 0]}

### bestalbum에 담긴 곡들의 고유번호 추출
for i in bestalbum :
    for j in range(len(bestalbum[i])) :
        answer.append(bestalbum[i][j])

print(answer)