def solution(record):
    answer = []
    users = dict()

    for command in record:
        status, *user = command.split()
        if status in ('Enter', 'Change'):
            users[user[0]] = user[1]  # 'Enter'와 'Change'는 닉네임 갱신

    for command in record:
        status, *user = command.split()
        if status == 'Enter':
            answer.append(f'{users[user[0]]}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{users[user[0]]}님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))