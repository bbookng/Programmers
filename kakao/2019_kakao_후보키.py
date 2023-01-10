from itertools import combinations

def solution(relation):
    candidate_key = []
    unique = []

    for i in range(1, len(relation[0])):
        candidate_key.extend(combinations([j for j in range(len(relation[0]))], i))

    for candidate in candidate_key:
        tmp = [set([relate[i] for i in candidate]) for relate in relation]
        print(candidate)
        print(tmp)

        if len(tmp) == len(relation):






    return candidate

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))