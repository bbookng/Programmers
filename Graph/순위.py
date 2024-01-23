def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for result in results:
        graph[result[0]][result[1]], graph[result[1]][result[0]] = 1, -1

    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1

    for i in range(n+1):
        count = 0
        for j in range(n+1):
            if graph[i][j]:
                count += 1
        if count == n-1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))