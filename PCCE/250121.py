def make_standard(ext):
    if ext == "code":
        return 0
    if ext == "date":
        return 1
    if ext == "maximum":
        return 2
    if ext == "remain":
        return 3

def solution(data, ext, val_ext, sort_by):
    answer = []

    for row in data:
        std = make_standard(ext)
        if row[std] < val_ext:
            answer.append(row)

    return sorted(answer, key = lambda x: (x[make_standard(sort_by)]))