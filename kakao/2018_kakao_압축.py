def solution(msg):
    answer = []
    dic = {chr(i+64): i for i in range(1, 27)}

    for i in range(len(msg)):
        if msg[i] in dic.values():
            answer.append(ord(msg[i])-64)

        for j in range(i, len(msg)):
            if msg[i:j] in dic.values():
                answer.append(ord(msg[i]) - 64)



    return answer

print(solution("KAKAO"))