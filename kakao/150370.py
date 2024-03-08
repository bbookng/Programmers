def solution(today, terms, privacies):
    answer = []

    # 하나의 숫자 단위로 치환해서 계산하기.
    year, month, day = map(int, today.split("."))
    today = year * 28 * 12 + (month - 1) * 28 + day

    periods = dict()

    for term in terms:
        type, period = term.split()
        periods[type] = int(period) * 28

    for idx, privacy in enumerate(privacies):
        collection_date, type = privacy.split()
        year, month, day = map(int, collection_date.split("."))

        collection_date = year * 28 * 12 + (month - 1) * 28 + day

        std_date = collection_date + periods[type]

        print(std_date, today)

        if std_date <= today:
            answer.append(idx + 1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))