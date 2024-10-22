from collections import deque

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    sizes = [0] * (m + 1)

    def bfs(x, y):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        q = deque([(x, y)])
        visited[x][y] = 1

        size = 0
        min_y, max_y = y, y

        while q:
            x, y = q.popleft()

            size += 1
            min_y = min(min_y, y)
            max_y = max(max_y, y)

            for xx, yy in zip(dx, dy):
                nx, ny = x + xx, y + yy

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = 1

        for i in range(min_y, max_y + 1):
            sizes[i] += size

        print(sizes)

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                if not visited[i][j]:
                    bfs(i, j)

    return max(sizes)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))