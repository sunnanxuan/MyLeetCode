# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        pre=0
        stack=[]
        while stack1 and stack2:
            cur=stack1.pop()+stack2.pop()+pre
            stack.append(cur%10)
            pre=cur//10
        stack3=stack1 or stack2
        while stack3:
            cur=stack3.pop()+pre
            pre=cur//10
            stack.append(cur%10)
        if pre:
            stack.append(pre)
        root=node=ListNode(stack.pop())
        while stack:
            node.next=ListNode(stack.pop())
            node=node.next
        return root
