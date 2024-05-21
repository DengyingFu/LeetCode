# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #双指针法
        pre = None  #前一个指针
        cur = head #后一个指针
        while cur:
            temp = cur.next #先保存
            cur.next = pre
            pre = cur
            cur = temp
        return left
