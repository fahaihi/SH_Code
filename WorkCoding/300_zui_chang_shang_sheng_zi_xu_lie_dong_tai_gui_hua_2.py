class Solution:
    def func(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

my_solution = Solution()
ans = my_solution.func([1,2,3,4,5,7,6,3])
print(ans)