

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        # 使用DFS方法
        def dfs(i, j):
            # 定义函数出口
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            # 遍历周围的数据，并插旗
            grid[i][j] = '2'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        # 逐行遍历
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # 入口
                    dfs(i, j)
                    ans += 1
        return ans
my_solution = Solution()
print(my_solution.numIslands(grid))