# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        value = []
        cur = head
        while cur:
            value.append(cur.val)
            cur = cur.next
        value.sort()
        dummy = node = ListNode(0)
        for val in value:
            node.next = ListNode(val)
            node = node.next
        return dummy.next
