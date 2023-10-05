# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        cur = head
        l = 1
        while cur.next:
            cur = cur.next
            l += 1
        tail = cur
        k %= l
        if k == 0: return head
        cur = head
        pre = None
        n = 1
        while n <= l - k:
            pre = cur
            cur = cur.next
            n += 1
        pre.next = None
        tail.next = head
        return cur
