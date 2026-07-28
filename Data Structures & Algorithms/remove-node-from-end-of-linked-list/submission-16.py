class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # use a dummy node to simplify edge cases
        slow, fast = dummy, dummy
        
        # Move fast n+1 steps ahead so that slow lands on the node before the one to delete
        for _ in range(n+1):
            if fast:
                fast = fast.next
        
        # Move both pointers until fast hits the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next  # return dummy.next in case head was removed
