def solution(N, stages):
    results = [0] * N
    answer = []
    user_count = len(stages)

    for stage in stages:
        if stage > N:
            continue
        results[stage - 1] += 1

    for idx, result in enumerate(results):
        # user_count가 0일 경우 실패율을 0으로 처리
        if user_count == 0:
            answer.append([0, idx + 1])
        else:
            answer.append([result / user_count, idx + 1])
        user_count -= result

    answer = sorted(answer, key=lambda x: (-x[0], x[1]))

    return [x[1] for x in answer]