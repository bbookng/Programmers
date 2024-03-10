def recursive(idx, possibility, visited):
    global max_value

    # 가지치기
    if max_value >= possibility:
        return

    # 종료조건
    if idx == n:
        max_value = possibility


    # 다음거 결정
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            recursive(idx+1, possibility * possibilities[idx][i], visited)
            visited[i] = 0

tc = int(input())

for T in range(1, tc+1):
    max_value = 0
    n = int(input())
    possibilities = [list(map(lambda x: int(x)/100, input().split())) for _ in range(n)]
    recursive(0, 1, [0] * n)
    max_value = round(max_value * 100, 6)
    print(f"#{T} {max_value}")

