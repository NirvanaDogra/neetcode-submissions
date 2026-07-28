# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        if head.next == None:
            return head
            
        pos1 = head
        pos2 = head.next
        head.next = None
        print(pos1.val, pos2.val)
        while pos2.next!=None:
            pos3 = pos2.next
            pos2.next = pos1
            pos1 = pos2
            pos2 = pos3
        

            print(pos1.val, pos2.val)
        pos2.next = pos1
        return pos2
        