def solution(n, computers):
    answer = 0
    visited = [0] * n
    def dfs(node, computers):
        visited[node] = 1
        for i in range(len(computers)):
            if not visited[i] and computers[node][i] == 1:
                visited[i] = 1
                dfs(i, computers)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))