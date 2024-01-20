from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[1] = 0
    q = deque([1])

    while q:
        now = q.popleft()

        for i in graph[now]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[now] + 1

    for i in distance:
        if i == max(distance):
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))