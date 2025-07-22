class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 如果当前值是p或者q或者空，返回当前值
        if root is None or root.val == p or root.val == q:
            return root
        # 如果两个值都小于当前值，说明在左，或者在右，或者就是当前值
        if root.val > p and root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p and root.val < q:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

def build_BST():
    # 构建如下二叉搜索树：
    #        6
    #      /   \
    #     2     8
    #    / \   / \
    #   0  4  7  9
    #     / \
    #    3   5

    nodes = {i: TreeNode(i) for i in [0,1,2,3,4,5,6,7,8,9]}
    nodes[6].left = nodes[2]
    nodes[6].right = nodes[8]
    nodes[2].left = nodes[0]
    nodes[2].right = nodes[4]
    nodes[4].left = nodes[3]
    nodes[4].right = nodes[5]
    nodes[8].left = nodes[7]
    nodes[8].right = nodes[9]

    return nodes[6]  # root 节点是 6



def test_LCA():
    root = build_BST()
    sol = Solution()

    queries = [
        (2, 8),   # → 公共祖先是 6
        (2, 4),   # → 公共祖先是 2
        (3, 5),   # → 公共祖先是 4
        (0, 5),   # → 公共祖先是 2
        (7, 9),   # → 公共祖先是 8
        (0, 9),   # → 公共祖先是 6
        (6, 9),   # → 公共祖先是 6（自己就是）
    ]

    for p_val, q_val in queries:
        lca = sol.lowestCommonAncestor(root, p_val, q_val)
        print(f"LCA of {p_val} and {q_val} is: {lca.val}")

test_LCA()