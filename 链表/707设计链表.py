class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    #注意index从0开始
    def __init__(self):
        self.dummy = ListNode()  #虚拟头节点
        self.size = 0 #节点数

    def get(self, index: int) -> int:
        if index<0 or index>self.size-1:  
            return -1
        cur = self.dummy.next  #遍历的当前节点，从head头节点开始
        while index:  #这里判断是否正确的方法，取极端情况index=0时，正确则正确
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val=val,next=self.dummy.next)
        self.dummy.next = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy   #判断当前节点的next，所以初始化为虚拟头节点，cur.next=val时可以改cur.next
        newnode = ListNode(val=val)
        while cur.next!=None:
            cur = cur.next
        cur.next = newnode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:  #注意这里的index可以是size，即在尾部插入
            return 
        newnode = ListNode(val=val)
        cur = self.dummy
        while index:
            cur = cur.next
            index-=1
        newnode.next = cur.next
        cur.next = newnode
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>self.size-1:
            return 
        cur = self.dummy
        while index:
            cur = cur.next
            index-=1
        cur.next = cur.next.next
        self.size-=1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
