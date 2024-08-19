class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If you rotate k = len(list) you have the same list
        # k / len(list) rotations you can ignore
        # apply len(list) mod k rotations 
        #  5 > 4 > 7 > 8 > 3 > 2 > 1
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Determine the length of the linked list and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Compute the effective number of rotations needed
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the new tail (which will be the (length - k)th node)
        new_tail_position = length - k
        new_tail = head
        for _ in range(new_tail_position - 1):
            new_tail = new_tail.next

        # Step 4: Set the new head to be the node after the new tail
        new_head = new_tail.next

        # Step 5: Break the list at the new tail and link the old tail to the old head
        new_tail.next = None
        tail.next = head

        return new_head
