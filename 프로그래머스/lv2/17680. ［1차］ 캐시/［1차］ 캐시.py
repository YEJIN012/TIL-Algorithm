# 캐시에 들어오는 순서대로 오랫동안 참조되지 않은 캐시를 교체해줘야 함.
# 즉 index 0 을 교체하기로 함.
# 캐시가 참조되면 꺼내서 index -1로 옮겨준다.
def solution(cacheSize, cities):
    answer = 0
    # cities =  [city.lower() for city in cities]
    cities = list(map(lambda x: x.lower(), cities))

    cache = []
    time = 0
    for city in cities :
        # cache hit
        if city in cache :
            i = cache.index(city)
            cache.pop(i)
            cache.append(city)
            time += 1
        # cache miss
        else :
            if cacheSize > 0 :
                if len(cache) == cacheSize  :
                    cache.pop(0)
                cache.append(city)
            time += 5
    return time