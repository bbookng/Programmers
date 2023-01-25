import re

def solution(user_id, banned_id):
    global answered

    answered = []
    bans = []

    for ban in banned_id:
        l = len(ban)
        ban = ban.replace('*','\S')
        p = re.compile\
            (ban)
        bans.append((l, p))


    def backtracking(i, visited):
        global answered

        if i == len(banned_id):
            if visited not in answered:
                answered.append(visited)
            return

        for j in range(len(user_id)):
            if not (1 << j) & visited and bans[i][1].match(user_id[j]) and bans[i][0] == len(user_id[j]):
                visited += 2 ** j
                backtracking(i+1, visited)
                visited -= 2 ** j

    backtracking(0, 0)

    answer = len(answered)
    return answer