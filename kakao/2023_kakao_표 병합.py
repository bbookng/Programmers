from pprint import pprint


def update(r, c, nr, nc, table):
    if table[r][c][1] == [r, c]:
        table[r][c] = [table[nr][nc][0], [table[nr][nc][1][0], table[nr][nc][1][1]]]
    else:
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == table[r][c][1]:
                    table[i][j] = [table[nr][nc][0], [table[nr][nc][1][0], table[nr][nc][1][1]]]

def solution(commands):
    answer = []
    table = [[['', [r, c]] for c in range(51)] for r in range(51)]

    for command in commands:
        command = command.split()
        command, value = command[0], command[1:]

        if command == 'UPDATE' and len(value) == 3:
            r, c, value = int(value[0]), int(value[1]), value[2]
            if r == table[r][c][1][0] and c == table[r][c][1][1]:
                table[r][c][0] = value
                continue
            nr, nc = table[r][c][1]
            for i in range(1, 51):
                for j in range(1, 51):
                    if table[i][j][1] == [nr, nc]:
                        table[i][j][0] = value

        elif command == 'UPDATE' and len(value) == 2:
            value1, value2 = value[0], value[1]
            for i in range(1, 10):
                for j in range(1, 10):
                    if table[i][j][0] == value1:
                        table[i][j][0] = value2

        elif command == 'MERGE':
            r1, c1, r2, c2 = int(value[0]), int(value[1]), int(value[2]), int(value[3])
            if r1 == r2 and c1 == c2:
                continue
            if table[r1][c1][0] != '' and table[r2][c2][0] != '':
                update(r2, c2, r1, c1, table)
            elif table[r1][c1][0] == '' and table[r2][c2][0] != '':
                update(r1, c1, r2, c2, table)
            elif table[r1][c1][0] != '' and table[r2][c2][0] == '':
                update(r2, c2, r1, c1, table)
            else:
                table[r2][c2] = ['', [table[r1][c1][1][0], table[r1][c1][1][1]]]

        elif command == 'UNMERGE':
            r, c = int(value[0]), int(value[1])
            nr, nc = table[r][c][1]
            tmp = []
            for i in range(1, 51):
                for j in range(1, 51):
                    if i == r and j == c:
                        table[i][j] = [table[i][j][0], [i, j]]
                    elif [nr, nc] == table[i][j][1]:
                        table[i][j] = ['', [i, j]]

        elif command == 'PRINT':
            r, c = int(value[0]), int(value[1])
            if table[r][c][0] == '':
                answer.append("EMPTY")
            else:
                answer.append(table[r][c][0])

    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
