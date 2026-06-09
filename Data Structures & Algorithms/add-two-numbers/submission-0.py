# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy

        while l1 or l2 or carry: # We want to add a new digit if we still have a value in that place or a carry
            
            # Get the value of current number place if it exists
            s1 = l1.val if l1 else 0
            s2 = l2.val if l2 else 0

            # Sum up our values, get the carry and the digit for this current place
            newCarry, digit = divmod(s1 + s2 + carry,10)

            #If we have a next pointer, move them.
            if l1 :
                l1 = l1.next
            if l2:
                l2 = l2.next

            # Append our digit for this number place to our  result
            tail.next = ListNode(digit)
            tail = tail.next
            # Update carry for the next operation
            carry = newCarry

        # Return our result
        return dummy.next