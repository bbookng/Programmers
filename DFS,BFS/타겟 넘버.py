def dfs(numbers, target, idx, sum):
    global answer
    if idx == len(numbers):
        if sum == target:
            answer += 1
    else:
        dfs(numbers, target, idx + 1, sum + numbers[idx])
        dfs(numbers, target, idx + 1, sum - numbers[idx])

def solution(numbers, target):
    global answer
    answer = 0

    dfs(numbers, target, 0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))