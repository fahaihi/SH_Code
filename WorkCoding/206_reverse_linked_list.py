# 1. 定义 ListNode 类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. 构建原始链表：1 -> 2 -> 3 -> 4 -> 5
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 3. 打印链表用于验证
def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" → ".join(vals))

# 4. 使用你的 Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

# 5. 测试逻辑
values = [1, 2, 3, 4, 5]
head = build_linked_list(values)
print("原链表:")
print_linked_list(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("反转后链表:")
print_linked_list(reversed_head)
