def solution(record):
    answer = []
    result = []
    users = dict()
    for i in record:
        status, *user = i.split()
        if status == 'Enter':
            users[user[0]] = user[1]
            answer.append(f"{user[0]}님이 들어왔습니다.")
        elif status == 'Leave':
            answer.append(f"{user[0]}님이 나갔습니다.")
        elif status == 'Change':
            users[user[0]] = user[1]

    for i in answer:
        for key, value in users.items():
            if key in i:
                tmp = i.replace(key, value)
                result.append(tmp)
                break

    return result


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))