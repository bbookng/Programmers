from itertools import permutations

def caculater(num1, num2, operator):
    num1, num2 = int(num1), int(num2)
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return  str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)

def caculate(expression, tmp):
    cal = []

    for i in expression:
        if i not in tmp:
            if cal and cal[-1] not in tmp:
                cal[-1] = cal[-1] + i
            else:
                cal.append(i)
        else:
            cal.append(i)

    stack = []
    result = []

    for operator in tmp:
        while True:
            if len(cal) == 0:
                break
            now = cal.pop(0)
            if now == operator:
                stack.append(caculater(stack.pop(-1), cal.pop(0), operator))
            else:
                stack.append(now)
        result.append(int(stack[-1]))
        cal = stack
        stack = []

    return abs(int(result[-1]))

def solution(expression):
    answer = 0
    operators = list(permutations(['+', '-', '*'], 3))

    for i in operators:
        answer = max(answer, abs(int(caculate(expression, i))))

    return answer

print(solution("100-200*300-500+20"	))

'''
테스트 1 〉	통과 (0.10ms, 10.5MB)
테스트 2 〉	통과 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.17ms, 10.5MB)
테스트 4 〉	통과 (0.18ms, 10.3MB)
테스트 5 〉	통과 (0.14ms, 10.5MB)
테스트 6 〉	통과 (0.15ms, 10.5MB)
테스트 7 〉	통과 (0.16ms, 10.5MB)
테스트 8 〉	통과 (0.34ms, 10.4MB)
테스트 9 〉	통과 (0.34ms, 10.4MB)
테스트 10 〉	통과 (0.39ms, 10.3MB)
테스트 11 〉	통과 (0.24ms, 10.4MB)
테스트 12 〉	통과 (0.24ms, 10.4MB)
테스트 13 〉	통과 (0.40ms, 10.6MB)
테스트 14 〉	통과 (0.32ms, 10.5MB)
테스트 15 〉	통과 (0.61ms, 10.4MB)
테스트 16 〉	통과 (0.10ms, 10.5MB)
테스트 17 〉	통과 (0.22ms, 10.5MB)
테스트 18 〉	통과 (0.10ms, 10.4MB)
테스트 19 〉	통과 (0.15ms, 10.5MB)
테스트 20 〉	통과 (0.10ms, 10.4MB)
테스트 21 〉	통과 (0.30ms, 10.4MB)
테스트 22 〉	통과 (0.45ms, 10.5MB)
테스트 23 〉	통과 (0.08ms, 10.6MB)
테스트 24 〉	통과 (0.56ms, 10.5MB)
테스트 25 〉	통과 (0.62ms, 10.4MB)
테스트 26 〉	통과 (0.14ms, 10.4MB)
테스트 27 〉	통과 (0.42ms, 10.4MB)
테스트 28 〉	통과 (0.32ms, 10.5MB)
테스트 29 〉	통과 (0.58ms, 10.4MB)
테스트 30 〉	통과 (0.36ms, 10.5MB)
'''