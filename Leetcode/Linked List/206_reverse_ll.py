# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next #Temp variable for holding the rest of the line
            curr.next = prev 
            prev = curr 
            curr = next
        return prev # End up being the head

    # Continuous flipping of next using prev, curr, and next
    # to iteratively flip the LL


