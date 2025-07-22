
class Solution:
    def permute(self, nums):
        ans = []
        n = len(nums)
        path = [0] * n  # 记录当前遍历的字符
        def dfs(i, s):
            # i 表示抽取的第几个字符
            # s 表示剩余的字符空间
            if i == n:
                ans.append(path.copy())
                return
            for x in s:
                path[i] = x
                dfs(i + 1, s - {x})

        dfs(0, set(nums))
        return ans

mySolution = Solution()
res = mySolution.permute(['A', 'C', 'G', 'T'])
res.sort()
print(res)
