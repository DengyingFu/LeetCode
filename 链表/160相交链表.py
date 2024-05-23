# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 #双指针
      #思路1：两个指针分别从headA和headB开始，如果有相交设相交开始后面共有t个节点，那么指针pA和pB都是走skipA+skipB+t步就到相交点，那么可以通过判断
      #pA是否等于pB来判断是否走到了相交点。但是需要判断没有相交节点的情况及时跳出while循环，我这里的方法是判断pA和pB回头了几次，如果大于1次那么就代表没有相交点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
         pA = headA
        pB = headB
        na =nb= 0
        while pA!=pB:
            if pA.next!=None:
                pA = pA.next 
            else:
                pA = headB
                na+=1
            if pB.next!=None:   
                pB = pB.next 
            else:
                pB = headA
                nb+=1
            if na>1 or nb > 1:
                return None
        return pA
   #思路2：代码随想录思路，先遍历A和B的长度la和lb，假设la>lb，然后让curA先移动la-lb步，然后curA和curB同时移动判断有没有相交点
  class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        lA = lB = 0
        while curA != None:
            lA += 1
            curA = curA.next
        while curB != None:
            lB += 1
            curB = curB.next
        
        curA = headA
        curB = headB
        for _ in range(abs(lA-lB)):
            if lA>lB:
                curA = curA.next
            else:
                curB = curB.next
        while curA!=None:
            if curA==curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None
        
