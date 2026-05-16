# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ll1, ll2 = headA, headB

        while (ll1 != ll2):
            ll1 = headB if ll1 == None else ll1.next
            ll2 = headA if ll2 == None else ll2.next

        return ll1
            
        