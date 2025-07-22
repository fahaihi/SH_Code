class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is p or root is q or root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        else:
            return right
def build_test_tree():
    # 构建如下二叉树：
    #         3
    #       /   \
    #      5     1
    #     / \   / \
    #    6  2  0   8
    #      / \
    #     7   4

    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    n3.left = n5
    n3.right = n1
    n5.left = n6
    n5.right = n2
    n2.left = n7
    n2.right = n4
    n1.left = n0
    n1.right = n8

    return n3, n5, n1, n4  # 返回 root 和几个节点供测试

def test_LCA():
    root, p, q, r = build_test_tree()
    sol = Solution()

    lca1 = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca1.val}")  # 应为 3

    lca2 = sol.lowestCommonAncestor(root, p, r)
    print(f"LCA of {p.val} and {r.val} is: {lca2.val}")  # 应为 5

test_LCA()
