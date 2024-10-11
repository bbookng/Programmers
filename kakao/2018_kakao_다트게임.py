def solution(dartResult):
    result = []

    tmp_number = ''

    for dart in dartResult:
        if dart.isdigit():
            tmp_number = tmp_number + dart
        else:
            if tmp_number != '':
                result.append(int(tmp_number))
                tmp_number = ''

        if dart.isalpha():
            if dart == 'D':
                result[-1] = result[-1] ** 2
            elif dart == 'T':
                result[-1] = result[-1] ** 3
        elif dart == '*':
            result[-1] *= 2
            if len(result) != 1:
                result[-2] *= 2
        elif dart == '#':
            result[-1] *= -1

    return sum(result)