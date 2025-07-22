class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthV1(self, root: TreeNode) -> int:
        if root is None: return 0
        l_len = self.maxDepthV1(root.left)
        l_right = self.maxDepthV1(root.right)
        return max(l_len, l_right) + 1

    def maxDepthV2(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, depth):
            if node is None:
                return 0
            nonlocal ans
            depth += 1
            ans = max(depth, ans)
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return ans

def build_test_tree():
    # 创建节点
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    # 构建结构
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7

    return node3  # 返回根节点

# 执行测试
if __name__ == "__main__":
    root = build_test_tree()
    sol = Solution()
    depth = sol.maxDepthV2(root)
    print(f"树的最大深度是: {depth}")  # 预期输出：3
