# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sp = ListNode(0, head)
        ep = sp

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            ep = ep.next

        ep.next = ep.next.next

        return sp.next
            

        
        