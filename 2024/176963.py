def solution(name, yearning, photo):
    answer = []
    scores = dict()
    for i in range(len(name)):
        scores[name[i]] = yearning[i]

    for record in photo:
        total = 0
        for p in record:
            if p in name:
                total += scores[p]
        answer.append(total)
    return answer