nums = [3,4,5,1,2]

print("hello world!")
class Solution(object):
    def findMin(self, nums):
                                                   # 定义 x = nums[mid]为要找的值
        left, right = 0, len(nums) - 1             # 使用[0, n-1]的闭区间
        while left < right:
            mid = left + (right - left) // 2       # 定义mid区间
            if nums[mid] > nums[right]:            # 说明此时整个数组被分成两段，且x位于第一段，而且最小值一定在x的右边
                left = mid + 1                     # 更新区间
            else:
                right = mid
        return nums[left]

my_solution = Solution()
print(my_solution.findMin(nums))