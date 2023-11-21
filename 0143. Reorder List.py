# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack=[]
        cur=head
        while cur:
            stack.append(cur)
            cur=cur.next
        l=len(stack)
        if l<=2:
            return head
        n=(l-1)//2
        tail=stack[-n-1]
        tail.next=None
        stack[:]=stack[-n:]
        cur=head
        while stack:
            add=stack.pop()
            nxt=cur.next
            cur.next=add
            cur=cur.next
            cur.next=nxt
            cur=cur.next
        return head