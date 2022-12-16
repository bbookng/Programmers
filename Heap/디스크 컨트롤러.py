import heapq

def solution(jobs):
    answer = 0

    request = -1
    total = 0
    cnt = 0

    controller = []

    while cnt != len(jobs):
        for job in jobs:
            if request < job[0] <= total:
                heapq.heappush(controller, (job[1], job[0]))

        if controller:
            job = heapq.heappop(controller)

            request = total
            total += job[0]
            answer += total - job[1]

            cnt += 1

        else:
            total += 1


    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))