# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tempHead = head
        slow, fast = tempHead, tempHead
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        revHead = slow.next
        prev = None
        while revHead is not None:
            nxtNode = revHead.next
            revHead.next = prev
            prev = revHead
            revHead = nxtNode
        
        slow.next = None
        
        head1 ,head2 = head, prev
        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head1 = nxt1

            head2.next = head1
            head2 = nxt2

# Question: https://leetcode.com/problems/reorder-list/