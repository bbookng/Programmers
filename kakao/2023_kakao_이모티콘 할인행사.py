# 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것
# 2. 이모티콘 판매액을 최대한 늘리는 것

# n 명의 사용자들에게 이모티콘 m 개를 할인하여 판매, 10 ~ 40 %

# 1. 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매
# 2. 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입

def make_cases(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in make_cases(array, r-1):
                print(array[i], next)
                yield [array[i]] + next


def solution(users, emoticons):
    plus_members, sales_revenue = 0, 0
    cases = make_cases((10, 20, 30, 40), len(emoticons))

    for case in cases:
        plus, profit = 0, 0

        for std, limit in users:
            total = 0
            for i, sale_percent in enumerate(case):
                if sale_percent >= std:
                    total += emoticons[i] * (1 - sale_percent / 100)

            if total >= limit:
                plus += 1
            else:
                profit += int(total)

        plus_members, sales_revenue = max([plus_members, sales_revenue], [plus, profit])

    return [plus_members, sales_revenue]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
