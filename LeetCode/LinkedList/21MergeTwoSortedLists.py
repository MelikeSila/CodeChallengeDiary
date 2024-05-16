# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1


        temp1 = list1
        temp2 = list2

        newList = ListNode()
        tempN = newList

        print(tempN)

        while temp1 and temp2:
            if temp1.val < temp2.val:
                tempN.val = temp1.val
                temp1 = temp1.next
            else:
                tempN.val = temp2.val
                temp2 = temp2.next
                
            tempN.next = ListNode()
            tempN = tempN.next
            print(newList)

        if temp2:
            tempN.val = temp2.val
            tempN.next = temp2.next
        elif temp1:
            tempN.val = temp1.val
            tempN.next = temp1.next

        return newList
                
            
