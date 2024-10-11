def make_binary_number(n, number):
    answer = ''

    while number:
        tmp = number % 2
        number //= 2
        answer = str(tmp) + answer
    return answer.zfill(n)


def solution(n, arr1, arr2):
    arr = [[' '] * n for _ in range(n)]

    for i, number in enumerate(arr1):
        binary_number = list(make_binary_number(n, number))
        for j, binary in enumerate(binary_number):
            if binary == str(1):
                arr[i][j] = '#'

    for i, number in enumerate(arr2):
        binary_number = list(make_binary_number(n, number))
        for j, binary in enumerate(binary_number):
            if binary == str(1):
                arr[i][j] = '#'

    return [''.join(line) for line in arr]