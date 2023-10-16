# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_l=dummy_l=ListNode(0)
        head_r=dummy_r=ListNode(0)
        cur=head
        while cur:
            if cur.val<x:
                dummy_l.next=cur
                dummy_l=dummy_l.next
            elif cur.val>=x:
                dummy_r.next=cur
                dummy_r=dummy_r.next
            cur=cur.next
        dummy_l.next=head_r.next
        dummy_r.next=None
        return head_l.next