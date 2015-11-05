#To Do:
#Fix print_backwards() - closer.  Fix add_at and add_first
class Node:
    def __init__(self,item=None,prev=None):
        self.item = item
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.item)

class CollectionTypeError(Exception):
    def __init__(self,msg=''):
        self.msg = "Wrong type for passed in collection, please use list"
    def __str__(self):
        return repr(self.msg)
        
        
class LinkedList:
    """
    Optionally takes in a list.
    """
    def __init__(self,collection=[]):
        try:
            if type(collection) != type(list()):
                raise CollectionTypeError
            else:
                pass
        except CollectionTypeError as col:
            print col

        if collection == []:
            self.length = 0
            self.head = None
        elif len(collection) == 1:
            self.length = 1
            self.head = Node(collection[0])
            self.head.next = None
            self.head.prev = None
        elif len(collection) < 3:
            self.length = len(collection)
            self.head = Node(collection[0])
            curr = Node(collection[1])
            curr.prev = self.head
            curr.next = None
            self.head.next = curr
        else:
            self.length = len(collection)
            self.head = Node(item=collection[0])
            self.head.next = None
            curr = Node(item=collection[1])
            curr.prev = self.head
            curr.next = None
            self.head.next = curr
            prev = curr
            for item in collection[2:]:
                curr = Node(item)
                curr.prev = prev
                prev.next = curr
                curr.next = None
                prev = curr
                
    def print_backwards(self):
        curr = self.head
        while curr != None:
            curr = curr.next
        while curr != None:
            print curr,
            curr = curr.prev
        
        
    def pretty_print(self):
        curr = self.head
        while curr:
            print curr,
            curr = curr.next
        print

    def add_first(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.head.item = new_node.item
            self.head.next = None
            self.head.prev = None
        else:    
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
        self.length += 1
        

    def add_last(self,item):
        if self.length == 0:
            self.add_first(item)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            new_node = Node(item)
            new_node.prev = curr
            curr.next = new_node
            new_node.next = None
            self.length += 1
        
    def add_at(self,item,location):
        if location == 0:
            self.add_first(item)
        else:    
            curr = self.head
            count = 0
            if location < self.length:
                while (curr != None) and (count < location):
                    curr = curr.next
                    count += 1
                new_node = Node(item)
                curr.prev.next = new_node
                new_node.next = curr
                self.length += 1
            else:
                raise Exception("location out of range")

    def contains(self,val):
        curr = self.head
        while curr:
            if curr.item == val:
                return True
            curr = curr.next
        return False

    def at_index(self,val):
        curr = self.head
        ind = 0
        while curr:
            if curr.item == val:
                return ind
            ind += 1
            curr = curr.next
            
        return False

    def remove_first(self):
        if self.length > 0: 
            curr = self.head 
            val = curr.item
            curr = curr.next
            self.head = curr
            self.length -= 1
            return val
        else:
            raise Exception("Empty list, cannot remove")
    
    def remove_last(self):
        if self.length > 0:
            curr = self.head
            while curr.next:
                curr = curr.next
            val = curr.item
            try:
                prev = curr.prev
                prev.next = None
            except AttributeError:
                pass
            curr.item = None
            curr.prev = None
            curr.next = None
            curr = None
            self.length -= 1
            return val
        else:
            raise Exception("Empty list, cannot remove")
    
    def clone(self):
        curr = self.head
        listing = []
        while curr:
            listing.append(curr.item)
            curr = curr.next
        return LinkedList(listing)


    def iterator(self):
        curr = self.head
        return curr

    def peek(self):
        return self.head.item
    
    def peek_last(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.item

    def remove(self,val):
        index = self.at_index(val) 
        if index == False and type(index) == type(bool()):
            return False
        curr = self.head
        if index == 0:
            self.head = curr.next
            curr.item = None
            curr = None
            
        elif index == self.length:
            self.head = curr.next
            while curr.next:
                curr = curr.next
            prev = curr.prev
            prev.next = None
            curr.item = None
            curr = None
        elif index < self.length:
            while index > 0:
                index -= 1
                curr = curr.next
            prev = curr.prev
            next_thing = curr.next
            prev.next = next_thing
            next_thing.prev = prev
            curr.item = None
            curr = None
    
    def to_list(self):
        listing = []
        curr = self.head
        while curr:
            listing.append(curr.item)
            curr = curr.next
        return listing

    def size(self):
        return self.length

#To Do: implement all of these methods:http://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html
