# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        resHead = res
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                newNode = ListNode(list1.val)
                res.next = newNode
                res = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                res.next = newNode
                res = newNode
                list2 = list2.next
        
        while list1 is not None:
            newNode = ListNode(list1.val)
            res.next = newNode
            res = newNode
            list1 = list1.next
        
        while list2 is not None:
            newNode = ListNode(list2.val)
            res.next = newNode
            res = newNode
            list2 = list2.next

        return resHead.next

# Question: https://leetcode.com/problems/merge-two-sorted-lists/