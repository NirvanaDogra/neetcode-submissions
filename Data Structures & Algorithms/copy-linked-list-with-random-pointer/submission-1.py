"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        if head == None:
            return head
            
        def duplicate(temp):
            if id(temp) in dic:
                # print("found")
                return dic[id(temp)]
            
                
            
        
            copy = Node(temp.val, None, None)
            dic[id(temp)] = copy
            print(copy.val)
           
            if temp.random==temp:
                copy.random = copy
            elif temp.random == None:
                copy.random = None
            else:
                copy.random = duplicate(temp.random)


            if temp.next ==None:
                copy.next=None
            else:
                copy.next = duplicate(temp.next)
            return copy
        temp = head
        return duplicate(temp)


       
