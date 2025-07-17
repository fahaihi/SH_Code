matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0) # 定义方向=> 右下左上

class Solution:
    def my_func(self, matrix):
        m, n = len(matrix), len(matrix[0])
        i = j = di = 0
        ans = []
        # 开始遍历所有的数目
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                # 到达边界，需要更改方向
                di = (di + 1) % 4
            i, j = i + DIRS[di][0], j + DIRS[di][1]
        return ans
my_solution = Solution()
print(my_solution.my_func(matrix))
print(my_solution.my_func([[1,2,3],[4,5,6],[7,8,9]]))