nums = [4,5,6,7,0,1,2]
target = 0

class Solution:
    def min_serch(self, nums):
        # 使用二分查找判断最小值所在的位置
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]: # 最小的值在x = nums[mid]的右边
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, nums, target, left, right):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def search(self, nums, target):
        # 定义两个函数，使用分段的二分查找
        if nums is None or nums == []:
            return -1
        pos = self.min_serch(nums)
        if target >= nums[pos] and target <= nums[-1]:
            return self.binary_search(nums, target, pos, len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, pos - 1)

my_solution = Solution()
print(my_solution.search([4,5,6,7,0,1,2], 0))
