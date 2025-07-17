nums = [-2,1,-3,4,-1,2,1,-5,4]

# 动态规划解法
# 动态规划dp[i]表示前i个位置的当前最优解
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], 0) + nums[i] # 要门前面是+的，要么是0，只能取这两种状态才能保证当前的最大
        return max(dp)
my_solution = Solution()
print(my_solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(my_solution.maxSubArray([5,4,-1,7,8]))