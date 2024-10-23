def solution(board, h, w):
    answer = 0
    n = len(board)

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    now_color = board[h][w]

    for dx, dy in direction:
        nx, ny = h + dx, w + dy
        if 0 <= nx < n and 0 <= ny < n:
            if now_color == board[nx][ny]:
                answer += 1

    return answer