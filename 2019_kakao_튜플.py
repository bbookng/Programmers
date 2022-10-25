from collections import deque

def solution(s):
    answer = []
    s = s[1:len(s)-1]

    s2 = []

    # tmp = []
    # numbers = ''
    #
    # flag = False
    #
    # for i in s:
    #     if i == '{':
    #         flag = True
    #     elif i == '}':
    #         tmp.append(numbers)
    #         numbers = ''
    #         s2.append(tmp)
    #         tmp = []
    #         flag = False
    #     if flag and i != '{':
    #         if i == ',':
    #             tmp.append(numbers)
    #             numbers = ''
    #         else:
    #             numbers += i


    s2.sort(key=lambda x:len(x))

    for i in s2:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))

    return(answer)






s = "{{20,111},{111}}"
print(solution(s))