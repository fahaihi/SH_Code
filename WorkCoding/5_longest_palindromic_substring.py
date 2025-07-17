s = "jdfhjrekhfjkrehbjkhkhabcdefkwwwrwwwkfedcbagekhk"

# 使用动态规划算法,定于状态dp[i][j]处所对应的字符串是否为回文串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True
        beg_, len_ = 0, 1
        for j in range(1, n) :       # 遍历列
            for i in range(0, j):    # 因为对角线已经填充，所哟一这里不需要管他
                if s[i] != s[j]:
                    dp[i][j] = False # 边边上的元素不一样
                else:
                    # 先判断特殊情况
                    if j - i + 1 < 4:# 判断子串=2或者=3
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 当此时位置为真的时候，说明是一个可能的解
                if dp[i][j] == True and j - i + 1 > len_:
                    len_ = j - i + 1
                    beg_ = i
        print("****************************" * 3, "\n")
        for i in dp:
            print(i)
        print("****************************" * 3, "\n")
        return s[beg_ : beg_ + len_]

my_solution = Solution()
print(my_solution.longestPalindrome("weabfbahi"))