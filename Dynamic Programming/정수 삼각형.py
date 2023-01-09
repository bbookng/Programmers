def solution(triangle):
    for i in range(len(triangle)-1, 0, -1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

    return triangle[0][0]

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.23ms, 10.1MB)
테스트 5 〉	통과 (1.58ms, 10.1MB)
테스트 6 〉	통과 (0.28ms, 10.2MB)
테스트 7 〉	통과 (0.91ms, 10.2MB)
테스트 8 〉	통과 (0.21ms, 10MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.23ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (30.91ms, 14.2MB)
테스트 2 〉	통과 (24.39ms, 13.1MB)
테스트 3 〉	통과 (36.11ms, 14.6MB)
테스트 4 〉	통과 (28.60ms, 14.2MB)
테스트 5 〉	통과 (29.66ms, 13.8MB)
테스트 6 〉	통과 (33.33ms, 14.7MB)
테스트 7 〉	통과 (31.14ms, 14.5MB)
테스트 8 〉	통과 (27.25ms, 13.6MB)
테스트 9 〉	통과 (29.38ms, 13.9MB)
테스트 10 〉	통과 (32.01ms, 14.4MB)

채점 결과
정확성: 64.3
효율성: 35.7
합계: 100.0 / 100.0
'''