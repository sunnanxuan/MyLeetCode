# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        cur = root
        n = 0
        stack = []
        while head and n < k:
            n += 1
            stack.append(head)
            head = head.next

            if n == k:
                while stack:
                    cur.next = stack.pop()
                    cur = cur.next
                n = 0
        if not stack:
            cur.next = None
        else:
            cur.next = stack.pop(0)
        return root.next
