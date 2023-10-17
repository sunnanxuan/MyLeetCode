# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        n=1
        root=pre=ListNode(0)
        while n<left:
            pre.next=cur
            pre=pre.next
            cur=cur.next
            n+=1
        stack=[]
        while n<=right:
            stack.append(cur)
            cur=cur.next
            n+=1
        tail=cur

        while stack:
            pre.next=stack.pop()
            pre=pre.next
        pre.next=tail
        return root.next