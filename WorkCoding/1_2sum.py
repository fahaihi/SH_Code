# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。结果唯一


nums = [3,2,4]
target = 6

class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for i, num in enumerate(nums):
            if target - num in my_dict:
                return [my_dict[target - num], i]
            my_dict[num] = i
mySolution = Solution()
print(mySolution.twoSum(nums, target))