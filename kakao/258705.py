def solution(n, tops):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = tops[0] + 3
    for i in range(1, n + 1):
        dp[i] = (dp[i-1] * (3 + tops[i-1]) - dp[i-2]) % 10007
    return dp[n]
