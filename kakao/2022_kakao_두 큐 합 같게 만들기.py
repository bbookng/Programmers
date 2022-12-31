from collections import deque

# test11, test28 시간초과 해결 안됨

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_1, sum_2 = sum(queue1), sum(queue2)
    cnt = 0

    while queue1 and queue2:
        if sum_1 == sum_2:
            return cnt

        if sum_1 > sum_2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum_1 -= tmp
            sum_2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum_1 += tmp
            sum_2 -= tmp
        cnt += 1

    return -1

