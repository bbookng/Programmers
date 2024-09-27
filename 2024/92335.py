def check(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    number = ''

    while n > 0:
        number = str(n % k) + number
        n //= k

    numbers = number.split('0')

    for num in numbers:
        if num and check(int(num)):
            answer += 1

    return answer

print(solution(437674, 3))