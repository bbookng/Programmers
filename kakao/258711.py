def solution(edges):
    answer = [0, 0, 0, 0]

    count = {}

    for a, b in edges:
        if not count.get(a):
            count[a] = [0, 0]
        if not count.get(b):
            count[b] = [0, 0]

        count[a][0] += 1
        count[b][1] += 1

    for key, cnt in count.items():
        if cnt[0] >= 2 and cnt[1] == 0:
            answer[0] = key
        elif cnt[0] == 0 and cnt[1] > 0:
            answer[2] += 1
        elif cnt[0] >= 2 and cnt[1] >= 2:
            answer[3] += 1

    answer[1] = (count[answer[0]][0] - answer[2] - answer[3])

    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))