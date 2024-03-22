# problems = [alp_req, cop_req, alp_rwd, cop_rwd, cost]

def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0

    for i in range(len(problems)):
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])

    if alp > max_alp:
        alp = max_alp
    if cop > max_cop:
        cop = max_cop

    dp = [[int(1e9)] * (max_alp+1) for _ in range(max_cop+1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            # 알고 1시간 공부
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            # 코딩 1시간 공부
            dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                new_alp = min(i + alp_rwd, max_alp)
                new_cop = min(j + cop_rwd, max_cop)
                if alp_req <= i and cop_req <= j:
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[-1][-1]