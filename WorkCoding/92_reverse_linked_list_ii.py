class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, start: int, end: int) -> ListNode:
        dummy = ListNode(next=head) # 构建一个辅助链表
        tmp = dummy                 # 找到辅助链表的上一个节点
        for _ in range(start - 1):
            tmp = tmp.next

        cur = tmp.next              # 找到left对应的节点
        pre = None                  # 辅助节点
        for _ in range(end - start + 1):  # 开始反转链表
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # 改改链表前后的位置
        tmp.next.next = cur
        tmp.next = pre
        return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

# 构建初始链表
values = [3, 1, 2, 3, 4, 5]
head = build_linked_list(values)
print_linked_list(head)
# 调用 reverseBetween
sol = Solution()
new_head = sol.reverseBetween(head, 2, 4)

# 打印结果

print_linked_list(new_head)
