# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        root=None
        if head:
            while cur and cur.next!=None:
                if cur.val!=cur.next.val:
                    if root==None:
                        root=cur
                        head=root
                    else:
                        root.next=cur
                        root=root.next
                    cur=cur.next
                elif cur.val==cur.next.val:
                    dummy=cur.next
                    while dummy and cur.val==dummy.val:
                        dummy=dummy.next
                    cur=dummy
            if cur and cur.next==None:
                if root==None:
                    root=cur
                    head=root
                else:
                    root.next=cur
                    root=root.next
        if root==None:
            return root
        else:
            root.next=None
        return head