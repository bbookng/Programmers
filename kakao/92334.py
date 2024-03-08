def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n

    name_dict = dict()
    idx_dict = dict()

    count_arr = [[0] * n for _ in range(n)]

    for idx, name in enumerate(id_list):
        name_dict[idx] = name
        idx_dict[name] = idx

    for record in report:
        giver, receiver = record.split()
        giver_idx, receiver_idx = idx_dict[giver], idx_dict[receiver]

        if not count_arr[receiver_idx][giver_idx]:
            count_arr[receiver_idx][giver_idx] = 1

    for i in range(n):
        if sum(count_arr[i]) >= k:
            for j in range(n):
                if count_arr[i][j]:
                    answer[j] += 1

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
