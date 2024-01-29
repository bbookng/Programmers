from collections import deque


def solution(tickets):
    answer = []
    dic = {}
    for ticket in tickets:
        department, destination = ticket[0], ticket[1]
        if department in dic:
            dic[department].append(destination)
        else:
            dic[department] = [destination]

    return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])