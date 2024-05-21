# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #虚拟头节点的方法
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next!=None and cur.next.next!=None:#注意搞清楚终止条件
            tmp1 = cur.next
            tmp2 = cur.next.next
            cur.next = cur.next.next  #因为这一步后获取不到1和3了，要先用tmp保存
            tmp1.next = tmp1.next.next
            tmp2.next = tmp1

            cur = cur.next.next
        return dummy.next
