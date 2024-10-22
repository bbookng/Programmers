def division(x):
    left, right = 0, 0

    for i in range(len(x)):
        if x[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = x[:i+1]
            v = x[i+1:]
            return u, v

def check(x):
    tmp = []
    for i in x:
        if i == '(':
            tmp.append(i)
        else:
            if not tmp:
                return False
            tmp.pop()

    if tmp:
        return False
    else:
        return True

def solution(p):
    if not p:
        return p

    u, v = division(p)

    if check(u):
        return u + solution(v)

    else:
        answer = '(' + solution(v) + ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    print(answer)
    return answer

print(solution("()))((()"))