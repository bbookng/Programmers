def solution(triangle):
    for i in range(len(triangle)-1, 0, -1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

    return triangle[0][0]

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.23ms, 10MB)
테스트 5 〉	통과 (0.92ms, 10.2MB)
테스트 6 〉	통과 (0.27ms, 10.2MB)
테스트 7 〉	통과 (1.03ms, 10.4MB)
테스트 8 〉	통과 (0.21ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 9.97MB)
테스트 10 〉	통과 (0.12ms, 9.97MB)

효율성  테스트
테스트 1 〉	통과 (28.28ms, 14.2MB)
테스트 2 〉	통과 (24.22ms, 13.1MB)
테스트 3 〉	통과 (32.36ms, 14.6MB)
테스트 4 〉	통과 (29.50ms, 14.1MB)
테스트 5 〉	통과 (29.27ms, 13.9MB)
테스트 6 〉	통과 (33.22ms, 14.7MB)
테스트 7 〉	통과 (33.68ms, 14.4MB)
테스트 8 〉	통과 (29.35ms, 13.6MB)
테스트 9 〉	통과 (26.73ms, 13.9MB)
테스트 10 〉	통과 (34.36ms, 14.4MB)

채점 결과
정확성: 64.3
효율성: 35.7
합계: 100.0 / 100.0
'''