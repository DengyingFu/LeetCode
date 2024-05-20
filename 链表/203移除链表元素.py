# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
         # 创建一个哑节点，简化头节点被删除的情况
        dummy = ListNode(next = head)

        pre = dummy  #前一节点
        cure = head  #当前节点
        while cure:  #当当前节点是空的时候就结束
            if cure.val == val:  #等于
                pre.next = cure.next  #就把前一个节点的next指向当前节点的next
            else:   
                pre = cure   #只有当不需要移除时，才更新pre。
            cure = cure.next
        return dummy.next  #注意返回的是dummy的next（head）
