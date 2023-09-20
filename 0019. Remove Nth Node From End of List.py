# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=1
        cur1=head
        while cur1.next:
            cur1=cur1.next
            l+=1
        t=l-n
        if t==0:return head.next
        else:
            cur2=head
            k=1
            while k<t:
                k+=1
                cur2=cur2.next
            cur2.next=cur2.next.next
        return head