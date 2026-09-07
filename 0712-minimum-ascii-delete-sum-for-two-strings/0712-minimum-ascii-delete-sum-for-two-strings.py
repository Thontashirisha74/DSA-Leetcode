class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # If s2 is empty, delete remaining characters of s1
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])

        # If s1 is empty, delete remaining characters of s2
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])

        # Fill DP table
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    delete_s1 = ord(s1[i]) + dp[i + 1][j]
                    delete_s2 = ord(s2[j]) + dp[i][j + 1]

                    dp[i][j] = min(delete_s1, delete_s2)

        return dp[0][0]