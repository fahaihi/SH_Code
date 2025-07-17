

nums = [7,1,5,3,6,4]
class Solution:
    def stock(self, prices):
        # 使用动态规划方法
        # 第一行表示买了当前的收益，第二行表示卖了或者从未买的收益
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)]
        # 初始化动态规划数组
        dp[0][0] = -prices[0] # 在第一天买了
        dp[0][1] = 0          # 没在第一天买
        m, n = len(dp), len(dp[0])
        print(m,n)

        for i in range(1, n): # 填充动态规划数组
            dp[i][0] = max(dp[i-1][0], -prices[i])            # 第i天持有股票
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i][0])  # 第i天不持有股票

        # 最后一天必然不持有
        return dp[n-1][1]

my_solution = Solution()
print(my_solution.stock([7,1,5,3,6,4]))