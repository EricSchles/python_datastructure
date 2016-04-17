class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.prev = prev
        self.next = next
    #comparator methods
    def __lt__(self,other):
        return self.data < other
    def __gt__(self,other):
        return self.data > other
    def __eq__(self,other):
        return self.data == other
    def __ge__(self,other):
        return self.data >= other
    def __le__(self,other):
        return self.data <= other
    def __ne__(self,other):
        return self.data != other
    def __str__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur
        self.size += 1
        
    def get_element(self,index):
        if not index <= self.size: raise Exception("Index out of range")
        cur = self.head
        counter = 0
        while index != counter and index <= self.size:
            cur = cur.next
            counter += 1
        return cur.data
            
    def get_index(self,data):
        index = 0
        cur = self.head
        while cur:
            if cur == data:
                return index
            else:
                cur = cur.next
                index += 1
        return -1
            
    def remove(self,data):
        if not self.head: return
        if self.head == data:
            cur = self.head
            self.head = cur.next
            cur.next = None
            cur = None
            return
        cur = self.head
        while cur.next:
            if cur == data:
                prev_node = cur.prev
                new_next = cur.next
                prev_node.next = new_next
                new_next.prev = prev_node
                cur = None
                break
            cur = cur.next
        if cur == data:
            prev_node = cur.prev
            prev_node.next = None
            cur = None
            
    def pprint(self):
        if not self.head: print
        cur = self.head
        while cur:
            print cur,
            cur = cur.next
        print 
            
if __name__ == '__main__':
    import random
    ll = LinkedList()
    [ll.append(random.randint(0,1000)) for _ in xrange(10)]
    ll.pprint()
    element = ll.get_element(0)
    ll.remove(element)
    ll.pprint()
                    
