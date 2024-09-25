# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values=[]
        cur=head
        while cur:
            values.append(cur.val)
            cur=cur.next
        res=[]
        stack=[]
        for v in values[::-1]:
            while stack and stack[-1]<=v:
                stack.pop()
            if not stack:
                res.append(0)
                stack.append(v)
            else:
                res.append(stack[-1])
                stack.append(v)
        return res[::-1]