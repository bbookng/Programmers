def solution(nodeinfo):
    answer = [[]]
    tree = dict()

    for i, node in enumerate(nodeinfo):
        tree[i] = (node[0], node[1])

    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))