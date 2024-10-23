def check(mat_size, x, y, max_x, max_y, park):
    for i in range(mat_size):
        for j in range(mat_size):
            if not 0 <= x + i < max_x or not 0 <= y + j < max_y:
                return False
            if park[x + i][y + j] != "-1":
                return False
    return True

def solution(mats, park):
    mats.sort(reverse=True)
    max_x = len(park)
    max_y = len(park[0])

    for mat in mats:
        for i in range(max_x):
            for j in range(max_y):
                if park[i][j] == "-1":
                    if check(mat, i, j, max_x, max_y, park):
                        return mat

    return -1

print(solution([5, 3, 2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))