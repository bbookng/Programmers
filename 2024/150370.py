def solution(today, terms, privacies):
    answer = []
    period = dict()
    year, month, day = map(int, today.split('.'))
    today = year * 12 * 28 + (month - 1) * 28 + day

    for term in terms:
        type, num = term.split(' ')
        period[type] = int(num) * 28

    for idx, privacy in enumerate(privacies):
        date, type = privacy.split(' ')
        year, month, day = map(int, date.split('.'))

        std_date = year * 12 * 28 + (month - 1) * 28 + day + period[type]

        if std_date <= today:
            answer.append(idx + 1)

    return answer