def solution(survey, choices):
    answer = ''

    count = {"R": 0, "T": 0,
             "C": 0, "F": 0,
             "J": 0, "M": 0,
             "A": 0, "N": 0}

    for i in range(len(survey)):
        disagree, agree = survey[i][0], survey[i][1]
        choice = choices[i]

        if choice < 4:
            count[disagree] += (4 - choice)
        elif choice > 4:
            count[agree] += (choice - 4)

    answer += "R" if count["R"] >= count["T"] else "T"
    answer += "C" if count["C"] >= count["F"] else "F"
    answer += "J" if count["J"] >= count["M"] else "M"
    answer += "A" if count["A"] >= count["N"] else "N"

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))