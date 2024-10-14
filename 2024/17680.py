from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque([])

    for city in cities:
        city = city.upper()

        if len(q) < cacheSize:
            if city not in q:
                q.append(city)
                answer += 5
            else:
                q.remove(city)
                q.append(city)
                answer += 1
        else:
            if city not in q:
                q.append(city)
                q.popleft()
                answer += 5
            else:
                q.remove(city)
                q.append(city)
                answer += 1

    return answer

print(solution(0, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	))