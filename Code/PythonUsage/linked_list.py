
#从后面插入
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node

        if self.last:
            self.last.next = new_node
            self.last = new_node
        else:
            self.last = new_node

    def __str__(self):
        res = "["
        cur = self.head
        while cur:
            res += str(cur.val) + ","
            cur = cur.next
        res += "]"
        return res



 #从前面插入   
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp




#mylist = UnorderedList()
#mylist.add(31)
#mylist.add(77)
#mylist.add(17)


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(5)
ll.add(9)
print(ll.head.next.next.val)
print(ll)


