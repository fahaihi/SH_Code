nums = [1,3,5,4,2]
# ==》 [1, 4, 2, 3, 5]
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # step1: 从右边向左边找到第一个数nums[i],其满足nums[i]<nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        print(nums[i], "\n")
        # step2: 找到稍微比nums[i]大一点的数nums[j]
        j = n - 1
        if i >= 0:
            while nums[i] >= nums[j]:
                j -= 1
            # 交换值
            print(nums[j], "\n")
            nums[i], nums[j] = nums[j], nums[i]

        # step3: 反转剩余的数
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

my_solu = Solution()
print(my_solu.nextPermutation(nums))