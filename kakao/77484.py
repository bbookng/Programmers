def solution(lottos, win_nums):
    result = [6, 6, 5, 4, 3, 2, 1]

    winnings = 0

    cnt = lottos.count(0)

    for num in lottos:
        if num in win_nums:
            winnings += 1

    return [result[winnings + cnt], result[winnings]]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))