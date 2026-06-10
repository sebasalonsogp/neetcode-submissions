# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. Split list in half using fast and slow
        # 2. Reverse second half of list
        # 3. Merge first half and reversed second half

        # (1) Split
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # ensure to sever first half from second half

        # (2) Reverse second

        prev = None
        cur = second

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        second = prev

        # (3) Merge first and second

        first = head
        # We go until we iterate thru second since once its done, the remaining elements of first
        # will be in correct position since first is always = or > than the len of second
        while second: 
            
            tmpF = first.next
            tmpS = second.next


            first.next = second
            second.next = tmpF

            first = tmpF
            second = tmpS

        


