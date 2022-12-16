import heapq

def solution(operations):
    answer = []

    for operation in operations:
        order, number = operation.split()
        if order == 'I':
            heapq.heappush(answer, int(number))
        else:
            if not answer:
                continue
            if number == '1':
                answer.remove(max(answer))
            else:
                heapq.heappop(answer)

    if not answer:
        return [0, 0]
    else:
        return [max(answer), min(answer)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

'''
테스트 1 〉	통과 (0.08ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
'''