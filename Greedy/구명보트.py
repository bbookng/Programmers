def solution(people, limit):
    boats = [0]
    for person in people:
        for i in range(len(boats)):
            if person + boats[i] <= limit:
                boats[i] += person
                break
        else:
            boats.append(person)

    return len(boats)

print(solution([70, 80, 50], 100))

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer