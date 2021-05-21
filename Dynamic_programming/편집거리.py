# 답지 확인 필요

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:  # 문자열이 다르다면 삭제, 교체, 삽입 중 가장 적은 방법 + 1
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

    return dp[n][m]


a = input()
b = input()

print(edit_dist(a, b))
