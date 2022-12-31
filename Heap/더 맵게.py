import heapq

def solution(scoville, K):
    if 0 in scoville or len(scoville) < 2:
        return -1
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 2:
            if heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) >= K:
                return answer + 1
            else:
                return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))