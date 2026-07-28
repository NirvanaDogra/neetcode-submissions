# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        head = ListNode(0, None)
        temp = head
        while l1!=None and l2!=None:
            if l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next
        
        if l1!=None:
            temp.next = l1
        if l2!=None:
            temp.next = l2
        
        return head.next


        