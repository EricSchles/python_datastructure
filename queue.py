class Queue:
    def __init__(self):
        self.listing = []
    def get(self):
        return self.listing.pop()
    def put(self,data):
        self.listing.insert(0,data)

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return repr(self.data)

class LL_Queue:
    def __init__(self):
        self.root = None
        self.tail = None
        self.size = 0
    def put(self,data):
        node = Node(data)
        node.next = self.root
        self.root.prev = node
        self.root = node
    def get(self):
        data = self.tail.data
        if self.tail.prev:
            cur = self.tail
            self.tail = cur.prev
            cur = None
        else:
            self.tail = None
        return data
