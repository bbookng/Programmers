from collections import deque

def solution(queue1, queue2):
    answer = 0

    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)

    while queue1 and queue2:
        if answer >= (len(queue1) + len(queue2)) * 2:
            return -1

        if sum1 == sum2:
            return answer

        if sum1 > sum2:
            tmp = queue1.popleft()
            sum1 -= tmp
            sum2 += tmp
            queue2.append(tmp)
        else:
            tmp = queue2.popleft()
            sum1 += tmp
            sum2 -= tmp
            queue1.append(tmp)

        answer += 1

    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))