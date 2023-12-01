# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_A = []
        stack_B = []
        curA = headA
        curB = headB
        while curA:
            stack_A.append(curA)
            curA = curA.next
        while curB:
            stack_B.append(curB)
            curB = curB.next
        a = b = None
        while a == b and (stack_A and stack_B):
            res = a
            a = stack_A.pop()
            b = stack_B.pop()
        if a == b:
            res = a
        return res
