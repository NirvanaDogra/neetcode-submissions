# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None 
        node = head # 0

        while node:
            after = node.next # 1
            node.next = pre # point to none
            pre = node # 0
            node = after # 1
            
        return pre