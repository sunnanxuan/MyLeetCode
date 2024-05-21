# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur=head
        n=0
        while cur:
            n+=1
            cur=cur.next
        m=n//k
        d=n%k
        res=[]
        while k and head:
            c=m
            cur=head
            if d>0:c+=1;d-=1
            while c:
                tail=cur
                cur=cur.next
                c-=1
            tail.next=None
            res.append(head)
            head=cur
            k-=1
        while k and not head:
            res.append(None)
            k-=1
        return res
