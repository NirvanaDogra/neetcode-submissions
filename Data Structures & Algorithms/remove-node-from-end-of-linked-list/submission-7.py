# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = None
        temp = head
        count = 0

        if slow.next == None and n ==1:
            return None

        while count<n:
            fast = temp.next
            temp = temp.next
            count+=1
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        if fast:
            slow.next = slow.next.next
        else:
            head = head.next

        return head