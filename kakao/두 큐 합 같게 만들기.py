from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    while answer <= (len(queue1) + len(queue2)) * 2:
        if sum1 == sum2:
            return answer
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp

        elif sum1 < sum2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        answer += 1

    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))