# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for cur in lists:
            while cur:
                values.append(cur.val)
                cur = cur.next
        values.sort()
        head = dummy = ListNode(0)

        for v in values:
            dummy.next = ListNode(v)
            dummy = dummy.next
        return head.next
