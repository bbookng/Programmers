def solution(key, lock):
    # 90도 회전
    def rotate(array):
        return list(zip(*array))[::-1]

    # 체크하기
    def check(x, y, total_size, start_index, end_index):
        arr = [[0] * size for _ in range(size)]

        for i in range(M):
            for j in range(M):
                arr[x + i][y + j] += key[i][j]

        for i in range(start_index, end_index + 1):
            for j in range(start_index, end_index + 1):
                arr[i][j] += lock[i - start_index][j - start_index]
                if arr[i][j] != 1:
                    return False

        return True

    M = len(key)
    N = len(lock)

    start_index = M - 1
    end_index = M + N - 2

    size = N + 2 * M - 2

    for _ in range(4):
        for i in range(end_index + 1):
            for j in range(end_index + 1):
                if check(i, j, size, start_index, end_index):
                    return True
        key = rotate(key)

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))