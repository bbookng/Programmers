def makeSet(String):
    arr = []
    for i in range(len(String)-1):
        if 'A' <= String[i] <= 'Z' and 'A' <= String[i+1] <= 'Z':
            arr.append((String[i] + String[i+1]))
    return arr

def solution(str1, str2):
    set1 = makeSet(str1.upper())
    set2 = makeSet(str2.upper())

    tmp = set1[:]
    union = len(set1)
    for i in set2:
        if i not in tmp:
            union += 1
        else:
            tmp.remove(i)

    tmp = set1[:]
    intersection = 0
    for i in set2:
        if i in tmp:
            intersection += 1
            tmp.remove(i)

    union = len(set1) + len(set2) - intersection
    answer = int(intersection/union * 65536) if union else 65536
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))