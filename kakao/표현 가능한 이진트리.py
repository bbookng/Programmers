def fill_number(number):
    tmp = 0
    while True:
        if 2 ** tmp-1 >= len(bin(number)[2:]):
            break
        tmp += 1
    return tmp

def check(number, p):
    mid = len(number) // 2
    if not p:
        if '1' in number:
            return 0

    if len(number) == 1:
        return number



    return check(number[mid+1:], int(number[mid])) and check(number[:mid], int(number[mid]))

def solution(numbers):
    answer = []
    for number in numbers:
        number = bin(number)[2:].zfill(2**fill_number(number)-1)
        answer.append(1 if check(number, int(number[len(number) // 2])) else 0)
    return answer

print(solution([7, 42, 5]))
print(solution([63, 111, 95]))