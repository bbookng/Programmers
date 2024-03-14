from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''

    x, y, r, c = x-1, y-1, r-1, c-1

    direction = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    q = deque([(x, y, 0, '')])
    while q:
        cx, cy, cnt, record = q.popleft()

        # 종료조건
        if cx == r and cy == c and cnt == k:
            return record

        for i in range(4):
            nx, ny, nd = cx + dx[i], cy + dy[i], direction[i]
            if abs(r-nx) + abs(c-ny) >= k - cnt:
                continue
            if 0 <= nx < n and 0 <= ny < m and cnt < k:
                q.append((nx, ny, cnt + 1, record + nd))
                break

    return "impossible"

print(solution(3, 4, 2, 3, 3, 1, 5))