class Solution:
    def editDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(dp[0])): dp[0][i] = i
        for j in range(len(dp)): dp[j][0] = j
        for i in range(1, m + 1):
             for j in range(1, n + 1):
                 if word1[i - 1] == word2[j - 1]:
                     dp[i][j] = dp[i - 1][j - 1]
                 else:
                     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

my_sol = Solution()
print(my_sol.editDistance("wabccf", "qqqtabcccccf"))