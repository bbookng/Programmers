import heapq

def solution(jobs):
    answer = 0

    request = -1
    now = 0
    cnt = 0

    controller = []

    while cnt != len(jobs):
        for job in jobs:
            if request < job[0] <= now:
                heapq.heappush(controller, (job[1], job[0]))

        if controller:
            job = heapq.heappop(controller)

            request = now
            now += job[0]
            answer += now - job[1]

            cnt += 1

        else:
            now += 1


    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))