# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# Note: x+y+z = y+z+x
class Solution:
    def intersect(self, l1, l2):
        p, q = l1, l2
        while p is not q:
            if p is not None: p = p.next
            else: p = l1
            if q is not None: q = q.next
            else: q = l2
        return p
    # p 和 q已经相交，返回谁都行

# 构造公共相交部分：8 → 4 → 5
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# 构造链表 A：4 → 1 → common
l1 = ListNode(4)
l1.next = ListNode(1)
l1.next.next = common

# 构造链表 B：5 → 6 → 1 → common
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(1)
l2.next.next.next = common

# 调用 intersect 函数
sol = Solution()
result = sol.intersect(l1, l2)

# 输出结果
print("相交节点的值是:", result.val if result else "无相交")
