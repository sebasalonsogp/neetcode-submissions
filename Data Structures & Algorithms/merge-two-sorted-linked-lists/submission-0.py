# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:

                if list1.val <= list2.val:
                        tail.next = list1
                        list1 = list1.next # move list1 pointer
                elif list2.val < list1.val:
                        tail.next = list2
                        list2 = list2.next #move list2 pointer
                
                tail = tail.next # move tail pointer 
        
        tail.next = list1 or list2 # append list with remaining elements to tail

        return dummy.next # return new head