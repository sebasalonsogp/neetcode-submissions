# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Target index = len(head) - n

        length = 0
        cur = head
        while cur:
            cur = cur.next
            length+=1
        
        index = length - n
        if index == 0:
            return head.next
        cur = head
        cnt = 0
        prev = None
        while cur:
            if cnt == index:
                prev.next = cur.next

            prev = cur
            cur=cur.next
            cnt+=1

        return head
        

