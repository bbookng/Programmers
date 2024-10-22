def solution(points, routes):
    answer = 0
    n = len(routes)  # 로봇의 수
    l = len(routes[0])  # 운송경로 길이
    idx = [0 for _ in range(n)]
    position = [[0, 0] for _ in range(n)]
    complete = [0 for _ in range(n)]

    while 1:
        pos_check = set()
        conflict = set()
        if sum(complete) == n:
            break
        for robot in range(n):
            i = idx[robot]
            # i == 0 이면 초기 위치 설정
            if i == 0:
                position[robot][0] = points[routes[robot][0] - 1][0]
                position[robot][1] = points[routes[robot][0] - 1][1]
            #                print(f"robot_{robot}: 초기 위치 설정 {position[robot]}")
            # i == l 이면 운송 완료
            elif i == l:
                complete[robot] = 1
                idx[robot] += 1
                #                print(f"robot_{robot}: 운송 완료")
                continue
            elif i > l:
                continue

            destination = points[routes[robot][i] - 1]
            # 로봇 이동
            if position[robot][0] != destination[0]:
                move = 1 if position[robot][0] < destination[0] else -1
                position[robot][0] += move
            #                print(f"robot_{robot}: 이동 {position[robot]} (destination: {destination})")
            elif position[robot][1] != destination[1]:
                move = 1 if position[robot][1] < destination[1] else -1
                position[robot][1] += move
            #                print(f"robot_{robot}: 이동 {position[robot]} (destination: {destination})")
            # 목적지에 도달한 경우
            if position[robot] == destination:
                idx[robot] += 1
            #                print(f"robot_{robot}: 목적지{i} 도달")

            # 충돌 여부 확인
            x, y = position[robot]
            if complete[robot]:
                continue
            if (x, y) in pos_check:
                conflict.add((x, y))
            else:
                pos_check.add((x, y))

        answer += len(conflict)

    return answer

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))