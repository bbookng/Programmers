def solution(diffs, times, limit):
    max_level = max(diffs)  # 최대 diff 구해두기
    l = 1
    r = max_level
    answer = max_level  # 정답이 max_diff인 경우를 대비해서 answer에 넣어두기

    while l < r:
        level = int((l + r) / 2)
        time = times[0]

        # 퍼즐 돌면서
        for i in range(1, len(diffs)):
            k = 0

            # 숙련도가 부족하면
            if level < diffs[i]:
                # 틀린 수
                k = diffs[i] - level

            # 퍼즐을 틀릴 때마다 현재 시간 + 이전 시간 * 틀린 갯수만큼, 그리고 맞았을 때
            time += (times[i] + times[i - 1]) * k + times[i]

        # 총 타임이 제한시간 이내면, r을 현재 레벨로 해서 범위 좁혀주기.
        if time <= limit:
            r = level
            answer = level
            # 구간이 좁아질때마다 항상 문제를 시간안에 풀 수 있는 r을 정답으로 설정
        else:
            # 제한시간을 넘어간다면 레벨 올려주기.
            l = level + 1
            # 현재 level은 정답이 아니므로 범위 자체에서 제외

    return answer