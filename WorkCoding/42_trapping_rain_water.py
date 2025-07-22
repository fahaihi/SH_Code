# 使用动态规划解法
# 当前位置的雨水取决于他自己的位置高度和前后柱子的高度

class Solution:
    def trap(self, height):
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        suf_max = [0] * n
        suf_max[-1] = height[-1]

        # 填充数组
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(pre_max[i], suf_max[i]) - height[i]

        return ans

my_solution = Solution()
print(my_solution.trap([1,8,6,2,5,4,8,3,7]))
print(my_solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))