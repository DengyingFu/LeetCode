# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#--------暴力法------------
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        size = 0
        while cur.next!=None: #先统计链表有多长
            cur = cur.next
            size+=1
        cur = dummy
        for _ in range(size-n): #循环找到要删除的节点的前一个节点作为cur
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
#----------双指针（快慢指针法）--------------
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = slow = dummy
        n = n+1
        while n and fast!=None:   #之所以n+1是因为cur要指向被删除节点的前一个节点，因此fast多走一步
            fast = fast.next        #因为可能n比链表长度大，因此也要判断fast不为None(不过题目已经说明n不超过链表长度，因此and fast!=None可删除，下面的if n==0:也可以删除)
            n -=1 
        while fast!=None:   
            fast = fast.next
            slow = slow.next
        if n==0:  #如果=0说明n是比链表长度小的
            slow.next = slow.next.next
        return dummy.next
