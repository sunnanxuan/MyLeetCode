# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        root = even = head.next
        while even and even.next:
            cur = even.next
            even.next = even.next.next
            even = even.next
            odd.next = cur
            odd = odd.next
        odd.next = root
        return head
