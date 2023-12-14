# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        pre = dummy = ListNode(0)
        dummy.next = head
        while cur:
            if cur.val == val:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return dummy.next
