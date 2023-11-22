# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        class Solution:
            def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                dummy = ListNode(-5001)
                stack_val = [-5001, 5001]
                stack = [dummy, None]
                cur = head
                while cur:
                    p = bisect.bisect(stack_val, cur.val)
                    inser = cur
                    cur = inser.next
                    pre = stack[p - 1]
                    pre.next = inser
                    inser.next = stack[p]
                    stack = stack[:p] + [inser] + stack[p:]
                    bisect.insort(stack_val, inser.val)
                return dummy.next