#给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
#同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
from sympy.physics.units import length


# 要点1）不能重复 -> 需要排序跳过
# 要点2）返回的是元素，不是下表
# 要点3）下标索引不能相等

class Solution:
    def threeSum(self, nums):
        len_ = len(nums)
        ans = []
        nums.sort()
        for i in range(len_ - 2):  # 需要留出两个元素的位置
            if i > 0 and nums[i] == nums[i - 1]: continue   # 去除第一个元素的重复位置
            j = i + 1                                       # 第二个元素的下标位置
            k = len(nums) - 1                               # 第三个元素的下标位置
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 < 0:      # 不足元素范围
                    j += 1
                elif sum3 > 0:    # 超出元素范围
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    # 开始向两端手速，不可能j和k对的元素还有答案
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]: k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
        return ans



nums = [-1,0,1,2,-1,-4]
my_solution = Solution()
print(my_solution.threeSum(nums))
