def solution(n, costs):
    answer = 0
    islands = [0] * n
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        land1, land2, fee = cost

        if islands.count(1) == n:
            break

        if not islands[land1] and not islands[land2]:
            islands[land1], islands[land2] = 1, 1
            answer += fee
        elif islands[land1] and not islands[land2]:
            islands[land2] = 1
            answer += fee
        elif not islands[land1] and islands[land2]:
            islands[land1] = 1
            answer += fee

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))