from collections import defaultdict
def solution(friends, gifts):
    k = len(friends)
    result = [0] * k

    name_array = dict()
    index_array = dict()

    present_rating = defaultdict(int)
    present_chart = [[0] * k for _ in range(k)]

    for i in range(k):
        for j in range(k):
            if i == j:
                present_chart[i][j] = -1

    for idx, name in enumerate(friends):
        name_array[idx] = name
        index_array[name] = idx

    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx, receiver_idx = index_array[giver], index_array[receiver]
        present_chart[giver_idx][receiver_idx] += 1
        present_chart[receiver_idx][giver_idx] -= 1

        present_rating[giver] += 1
        present_rating[receiver] -= 1

    for i in range(k):
        for j in range(k):
            if present_chart[i][j] > 0:
                result[i] += 1
            if present_chart[i][j] == 0:
                giver, receiver = name_array[i], name_array[j]
                if present_rating[giver] > present_rating[receiver]:
                    result[i] += 1

    return max(result)

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))