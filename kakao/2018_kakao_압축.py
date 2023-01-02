def solution(msg):
    answer = []

    # A부터 Z까지를 1부터 26으로 변환시켜주는 딕셔너리 생성
    d = {chr(i + 65): i + 1 for i in range(26)}
    # 다음 추가할 index 27
    idx = 27
    l = 0
    for i in range(len(msg)):
        # 그전에 2개 이상의 압축이 일어났으면 그거 넘어가는 과정
        if l > 2:
            l -= 1
            continue
        l = 1
        # dictionary에 msg[i:i+l]가 없을때까지 l을 1씩 늘려감.
        while i + l <= len(msg) and msg[i:i + l] in d:
            l += 1
        # anwer에 추가하고
        answer.append(d[msg[i:i + l - 1]])

        # 딕셔너리 업데이트
        d[msg[i:i + l]] = idx
        idx += 1

    return answer