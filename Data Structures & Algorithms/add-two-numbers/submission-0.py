# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one, two = l1, l2
        
        nodeHead = ListNode(0, None)
        temp = nodeHead
        carry = 0
        while one and two:
            s = sum([one.val, two.val, carry])
            print([one.val, two.val, carry])
            remainder = s%10
            carry = s//10
            temp.next = ListNode(remainder, None)
            temp = temp.next
            one = one.next
            two = two.next
        
        while one:
            s = sum([one.val, carry])
            remainder = s%10
            carry = s//10
            temp.next = ListNode(remainder, None)
            temp = temp.next
            one = one.next
        
        while two:
            s = sum([two.val, carry])
            remainder = s%10
            carry = s//10
            temp.next = ListNode(remainder, None)
            temp = temp.next
            two = two.next
        
        if carry > 0:
            temp.next = ListNode(carry, None)
        
        return nodeHead.next

            
