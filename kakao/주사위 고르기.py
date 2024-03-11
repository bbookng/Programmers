from itertools import combinations, product

def binary_search_win(left, right, target, arr):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def binary_search_lose(left, right, target, arr):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1

def solution(dice):
    answer = []
    max_value = 0

    # 1. 주사위 n/2 개씩 가져 가기 조합 만들기
    combi = list(combinations(range(len(dice)), len(dice) // 2))

    # 2. 가져간 주사위 6^n 합 만들기
    for i in range(len(combi) // 2 + 1):
        a = combi[i]
        b = combi[-i-1]

        sum_a = sorted(list(map(sum, product(*list(dice[j] for j in a)))))
        sum_b = sorted(list(map(sum, product(*list(dice[j] for j in b)))))

        a_win_count = 0
        b_win_count = 0

        for k in sum_a:
            a_win_count += binary_search_win(0, len(sum_b) - 1, k, sum_b)
            b_win_count += len(sum_b) - binary_search_lose(0, len(sum_b) - 1, k, sum_b)

        if a_win_count > max_value:
            max_value = a_win_count
            answer = a
        if b_win_count > max_value:
            max_value = b_win_count
            answer = b

    # 3. 이분탐색. (A를 기준으로 B를 돌면서 찾는다.)


    return list(map(lambda x:x + 1, list(answer)))

print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))