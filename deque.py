class DequeList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return repr(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        
    def _add_node(self,cur,data):
        new_node = Node(data)
        cur.next = new_node
        new_node.prev = cur
        
    def append(self,data):
        cur = self.head
        if not cur.next:
            self._add_node(cur,data)
            self.size += 1
        else:
            while cur.next:
                cur = cur.next
            self._add_node(cur,data)
            self.size += 1
            
    def pprint(self):
        cur = self.head
        while cur:
            print cur
            cur = cur.next

    def prepend(self,data):
        cur = self.head
        if not cur.next:
            self._add_node(cur,data)
            self.size += 1
        else:
            cur = self.head.next
            new_node = Node(data)
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = cur
            cur.prev = new_node
            self.size += 1
            
    def is_empty(self):
        if not self.head.next: return True
        else: return False

    def removeFront(self):
        cur = self.head
        if self.size >= 2:
            to_delete = cur.next
            new_next = cur.next.next
            new_next.prev = cur
            cur.next = new_next
            to_delete.next = None
            to_delete.prev = None
            to_delete = None
            self.size -= 1
        elif self.size == 1:
            cur.next = None
            self.size -= 1
            
    def removeBack(self):
        cur = self.head
        if self.size >= 2:
            while cur.next:
                cur = cur.next
            to_delete = cur
            second_to_last = cur.prev
            second_to_last.next = None
            to_delete.next = None
            to_delete.prev = None
            to_delete = None
            self.size -= 1
        if self.size == 1:
            cur = self.head
            cur.next = None
            self.size -= 1
class DequeLinkedList:
    def __init__(self):
        self.items = LinkedList()
