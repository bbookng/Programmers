def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver, pickup = 0, 0
    for i in range(n):
        deliver += deliveries[n-i-1]
        pickup += pickups[n-i-1]

        # cap 이 가용량이 있을 때 까지 (0, 0 이어야 cap 이 full)
        # 배달할 게 있거나, 픽업할 게 있을 때 까지.
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer += (n-i) * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))