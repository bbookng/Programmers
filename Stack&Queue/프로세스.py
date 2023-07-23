def solution(priorities, location):
    answer = 0
    q = [(i, p) for i, p in enumerate(priorities)]

    while True:
        now = q.pop(0)
        if any(now[1] < i[1] for i in q):
            q.append(now)
        else:
            answer += 1
            if now[0] == location:
                return answer