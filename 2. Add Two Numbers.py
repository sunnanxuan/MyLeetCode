# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1=l1
        cur2=l2
        cur=head=ListNode(0)
        p=0
        while cur1 and cur2:
            v=cur1.val+cur2.val+p
            p=0
            if v>=10:
                p=1
                v-=10
            cur.next=ListNode(v)
            cur=cur.next
            cur1=cur1.next
            cur2=cur2.next
        cur3=cur1 if cur1 else cur2
        while cur3 and p==1:
            v=cur3.val+p
            if v>=10:
                p=1
                v-=10
            else:p=0
            cur.next=ListNode(v)
            cur=cur.next
            cur3=cur3.next
        if cur3 and p==0:
            cur.next=cur3
        elif not cur3 and p==1:
            cur.next=ListNode(1)
        return head.next
