# 1. 이모티콘 플러스 가입자 최대한 늘리기
# 2. 이모티콘 판매액 최대한 늘리기

def make_case(arr, n, k, cases):
    percent = (10, 20, 30, 40)
    if k == n:
        cases.append(arr[:])
        return
    else:
        for i in percent:
            arr[k] += i
            make_case(arr, n, k+1, cases)
            arr[k] -= i

def solution(users, emoticons):
    n = len(emoticons)
    cases = []
    make_case([0] * n, n, 0, cases)

    plus_member, result = 0, 0

    for case in cases:
        emoticon_plus, profit = 0, 0

        for std_percent, deposit in users:
            total = 0
            for idx, sale in enumerate(case):
                if sale >= std_percent:
                    total += emoticons[idx] * (1 - sale / 100)

            if total >= deposit:
                emoticon_plus += 1
            else:
                profit += int(total)

        plus_member, result = max([plus_member, result], [emoticon_plus, profit])

    return [plus_member, result]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))