# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head
        last = None
        while actual is not None:
            sig_nodo = actual.next
            actual.next = last
            last = actual
            actual = sig_nodo

        return last


        