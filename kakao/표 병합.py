from pprint import pprint

def update(r, c, value, table):
    table[r][c][0] = value

def update_all(value, table, arr):
    for r, c in arr:
        table[r][c][0] = value

def merge(r1, c1, r2, c2, table, merge_dict):
    arr = []

    r, c = table[r1][c1][1]

    if table[r][c][0]:
        value = table[r][c][0]
    elif table[r2][c2][0]:
        value = table[r2][c2][0]
    else:
        value = ''

    if r2 < r1:
        tmp = r2
        r2 = r1
        r1 = tmp

    if c2 < c1:
        tmp = c2
        c2 = c1
        c1 = tmp

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            table[i][j][0] = value
            table[i][j][1] = [r, c]
            arr.append((i, j))

    if (r, c) in merge_dict.keys():
        merge_dict[(r, c)] += arr
    else:
        merge_dict[(r, c)] = arr

def unmerge(r, c, table, arr):
    for i, j in arr:
        table[i][j][1] = table[i][j][2]
        if i == r and j == c:
            continue
        else:
            table[i][j][0] = ''

def solution(commands):
    answer = []
    table = [[['', [r, c], [r, c]] for c in range(51)] for r in range(51)]
    merge_dict = dict()
    value_dict = dict()

    for command in commands:
        command = command.split()
        order, values = command[0], command[1:]

        # UPDATE 일 때
        if order == "UPDATE":
            # 하나의 셀만 업데이트를 할 때
            if len(values) == 3:
                r, c, value = int(values[0]), int(values[1]), values[2]
                parent_r, parent_c = table[r][c][1]

                if (parent_r, parent_c) in merge_dict.keys():
                    update_all(value, table, merge_dict[(parent_r, parent_c)])
                else:
                    update(r, c, value, table)
                    if value not in value_dict.keys():
                        value_dict[value] = [(r, c)]
                    else:
                        value_dict[value].append((r, c))

            # 전체 업데이트 할 때
            elif len(values) == 2:
                value1, value2 = values
                update_all(value2, table, value_dict.get(value1, []))
                if value2 not in value_dict.keys():
                    value_dict[value2] = value_dict.pop(value1)
                else:
                    value_dict[value2] += value_dict.pop(value1)

        # 병합할 때
        elif order == "MERGE":
            r1, c1, r2, c2 = map(int, values)
            # 같은 셀일 경우 무시
            if table[r1][c1][1] == table[r2][c2][1]:
                continue
            merge(r1, c1, r2, c2, table, merge_dict)

        # 병합 취소할 때
        elif order == "UNMERGE":
            r, c = map(int, values)
            merge_r, merge_c = table[r][c][1]
            unmerge(r, c, table, merge_dict[(merge_r, merge_c)])

        # 프린트 할 때
        else:
            r, c = int(values[0]), int(values[1])

            if table[r][c][0]:
                answer.append(table[r][c][0])
            else:
                answer.append("EMPTY")

    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))

def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    board = [["EMPTY"] * 50 for _ in range(50)]
    for command in commands:
        command = command.split(' ')
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r,c,value = int(command[1])-1,int(command[2])-1,command[3]
                x,y = merged[r][c]
                board[x][y] = value
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
        elif command[0] == 'MERGE':
            r1,c1,r2,c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1,y1 = merged[r1][c1]
            x2,y2 = merged[r2][c2]
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1,int(command[2])-1
            x, y = merged[r][c]
            tmp = board[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x,y):
                        merged[i][j] = (i,j)
                        board[i][j] = "EMPTY"
            board[r][c] = tmp
        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(board[x][y])
    return answer