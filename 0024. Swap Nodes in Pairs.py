# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root=ListNode(0)
        root.next=head
        cur=root
        while head:
            if head.next:
                nxt=head.next
                if head.next.next:
                    node=head.next.next
                else:
                    node=None
                cur.next=nxt
                nxt.next=head
                cur=head
                head.next=node
                head=head.next
            else:head=head.next
        return root.next

