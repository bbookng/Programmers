from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])

    while q:
        idx, total = q.popleft()

        if idx == len(numbers):
            if total == target:
                answer += 1
        else:
            q.append((idx + 1, total + numbers[idx]))
            q.append((idx + 1, total - numbers[idx]))

    return answer

print(solution([1, 1, 1, 1, 1], 3))