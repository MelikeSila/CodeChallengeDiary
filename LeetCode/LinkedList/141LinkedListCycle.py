# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        temp = head

        while temp:
            temp.val =-1000000
            if temp.next:
                temp = temp.next
                if temp.val <= -1000000:
                    return True
            else:
                return False
        
        return False