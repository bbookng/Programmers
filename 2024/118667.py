from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    limit = len(queue1) * 3
    answer = 0

    while answer <= limit:
        if sum1 == sum2:
            return answer

        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num

        answer += 1

    return -1