from collections import deque
def solution(x, y, n):
    q = deque([(x, 0)])
    visited = set()
    while q:
        i, j = q.popleft()
        if i > y or i in visited:
            continue
        visited.add(i)
        if i == y:
            return j
        for k in (i*3, i*2, i+n):
            if k <= y and k not in visited:
                q.append((k, j+1))
    return -1