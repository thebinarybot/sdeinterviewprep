# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of LL
        length = 0
        temphead = head
        while temphead:
            length += 1
            temphead = temphead.next
        
        # Remove from start
        n = length - n
        if n == 0:
            return head.next
        
        start = 0
        delete = head
        while n != start:
            start += 1
            delete = delete.next
        
        if delete.next is not None:
            deletenext = delete.next
        else:
            deletenext = None
        
        # Remove delete node
        temp = head
        while temp.next is not delete:
            temp = temp.next
        
        temp.next = deletenext
        delete.next = None

        return head

# Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/