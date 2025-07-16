from typing import List

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 使用DFS 方法
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            # 建立递归调用的出口
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans

my_solution = Solution()
print(my_solution.numIslands(grid))