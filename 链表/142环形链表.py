# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast!=None and fast.next!=None:#fast比slow快 因此判断fast就可以
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                idx1 = head
                idx2 = fast
                while idx1!=idx2:
                    idx1 = idx1.next
                    idx2 = idx2.next
                return idx1
        return None
