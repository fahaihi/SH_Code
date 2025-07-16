from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        ans = []
        #cur = [root]
        cur = deque([root])
        while cur:
            nxt = []
            tmp = []
            #for node in cur:
            for _ in range(len(cur)):
                node = cur.popleft()
                tmp.append(node.val)
                if node.left: cur.append(node.left)#nxt.append(node.left)
                if node.right: cur.append(node.right)#nxt.append(node.right)
            ans.append(tmp)
            #cur = nxt
        return ans

# 构造树结构
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

# 调用层序遍历
solution = Solution()
output = solution.levelOrder(root)

# 打印结果
print("层序遍历结果：", output)
