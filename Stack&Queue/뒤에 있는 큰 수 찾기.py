def solution(numbers):
    answer = [-1] * len(numbers)

    arr = []

    for idx in range(len(numbers)):
        target = numbers[idx]

        while arr and numbers[arr[-1]] < target:
            answer[arr.pop()] = target

        arr.append(idx)

    return answer