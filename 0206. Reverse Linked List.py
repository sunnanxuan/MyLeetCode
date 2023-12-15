# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=cur=ListNode(0)
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        while stack:
            node=stack.pop()
            cur.next=node
            cur=cur.next
        cur.next=None
        return dummy.next