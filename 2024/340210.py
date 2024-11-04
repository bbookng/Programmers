def calculate(num, base):
    total = 0
    for idx, digit in enumerate(num[::-1]):
        if digit.isdigit():
            total += int(digit) * (base ** idx)
    return total

def calculate2(num, base):
    if num == 0:
        return '0'
    digits = ''
    while num > 0:
        digits = str(num % base) + digits
        num //= base
    return digits

def get_max_digit(s):
    return max(int(c) for c in s if c.isdigit())

def solution(expressions):
    answer = []
    min_base = 2

    # 모든 수식에서 사용된 최대 자리수 + 1로 최소 진법 계산
    for expression in expressions:
        num1, operator, num2, _, result = expression.split(' ')
        max_digit = max(get_max_digit(num1), get_max_digit(num2))
        if result != 'X':
            max_digit = max(max_digit, get_max_digit(result))
        min_base = max(min_base, max_digit + 1)

    possible_bases = list(range(min_base, 10))

    # 결과가 주어진 수식을 사용하여 가능한 진법 필터링
    for expression in expressions:
        num1, operator, num2, _, result = expression.split(' ')
        if result == 'X':
            continue
        invalid_bases = []
        for base in possible_bases:
            num1_val = calculate(num1, base)
            num2_val = calculate(num2, base)
            result_val = calculate(result, base)
            if operator == '+':
                if num1_val + num2_val != result_val:
                    invalid_bases.append(base)
            else:
                if num1_val - num2_val != result_val:
                    invalid_bases.append(base)
        possible_bases = [b for b in possible_bases if b not in invalid_bases]

    # 결과가 지워진 수식 처리
    for expression in expressions:
        num1, operator, num2, _, result = expression.split(' ')
        if result != 'X':
            continue
        results = set()
        for base in possible_bases:
            num1_val = calculate(num1, base)
            num2_val = calculate(num2, base)
            if operator == '+':
                res_val = num1_val + num2_val
            else:
                res_val = num1_val - num2_val
            res_str = calculate2(res_val, base)
            results.add(res_str)
        if len(results) == 1:
            answer.append(f"{num1} {operator} {num2} = {results.pop()}")
        else:
            answer.append(f"{num1} {operator} {num2} = ?")

    return answer

def calculate(num, base):
    total = 0
    for idx, digit in enumerate(num[::-1]):
        if digit.isdigit():
            total += int(digit) * (base ** idx)
    return total

def calculate2(num, base):
    if num == 0:
        return '0'
    digits = ''
    while num > 0:
        digits = str(num % base) + digits
        num //= base
    return digits

def get_max_digit(s):
    return max(int(c) for c in s if c.isdigit())

def solution(expressions):
    answer = []
    min_base = 2

    # 모든 수식에서 사용된 최대 자리수 + 1로 최소 진법 계산
    for expression in expressions:
        num1, operator, num2, _, result = expression.split(' ')
        max_digit = max(get_max_digit(num1), get_max_digit(num2))
        if result != 'X':
            max_digit = max(max_digit, get_max_digit(result))
        min_base = max(min_base, max_digit + 1)

    possible_bases = list(range(min_base, 10))

    # 결과가 주어진 수식을 사용하여 가능한 진법 필터링
    for expression in expressions:
        num1, operator, num2, _, result = expression.split(' ')
        if result == 'X':
            continue
        invalid_bases = []
        for base in possible_bases:
            num1_val = calculate(num1, base)
            num2_val = calculate(num2, base)
            result_val = calculate(result, base)
            if operator == '+':
                if num1_val + num2_val != result_val:
                    invalid_bases.append(base)
            else:
                if num1_val - num2_val != result_val:
                    invalid_bases.append(base)
        possible_bases = [b for b in possible_bases if b not in invalid_bases]

    # 결과가 지워진 수식 처리
    for expression in expressions:
        num1, operator, num2, _, result = expression.split(' ')
        if result != 'X':
            continue
        results = set()
        for base in possible_bases:
            num1_val = calculate(num1, base)
            num2_val = calculate(num2, base)
            if operator == '+':
                res_val = num1_val + num2_val
            else:
                res_val = num1_val - num2_val
            res_str = calculate2(res_val, base)
            results.add(res_str)
        if len(results) == 1:
            answer.append(f"{num1} {operator} {num2} = {results.pop()}")
        else:
            answer.append(f"{num1} {operator} {num2} = ?")

    return answer
