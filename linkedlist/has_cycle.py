# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        if head and head.next:
            while (head.next):
                if head in visited:
                    return True
                else:
                    visited.add(head)
                    head = head.next
        else:
            return False
        return False