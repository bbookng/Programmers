def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.upper()

        if len(cache) < cacheSize:
            if city not in cache:
                cache.append(city)
                answer += 5
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1

        else:
            if city not in cache:
                cache.append(city)
                cache.pop(0)
                answer += 5
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1


    return answer

print(solution(5, ['jeju', 'pangyo', 'seoul', 'newyork', 'la', 'sanfrancisco', 'seoul', 'rome', 'paris', 'jeju', 'newyork', 'rome']))

