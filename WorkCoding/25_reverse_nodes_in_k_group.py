class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        tmp = dummy
        pre = None
        cur = head

        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = tmp.next
            tmp.next.next = cur
            tmp.next = pre
            tmp = nxt

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
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
head = build_linked_list(values)
print_linked_list(head)
# 调用 reverseBetween
sol = Solution()
new_head = sol.reverseKGroup(head, 3)
print_linked_list(new_head)