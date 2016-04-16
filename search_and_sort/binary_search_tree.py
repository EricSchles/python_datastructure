class Node:
    def __init__(self,data,right=None,left=None):
        self.data = data
        self.left = left
        self.right = right
        self.count = 1
    def __lt__(self,other):
        return self.data < other

    def __gt__(self,other):
        return self.data > other

    def __eq__(self,other):
        return self.data == other

    def __le__(self,other):
        return self.data <= other

    def __ne__(self,other):
        return self.data != other

    def __ge__(self,other):
        return self.data >= other
    
    def __str__(self):
        return repr(self.data)

class BinarySearchTree():
    def __init__(self):
        self.head = None
        self.size = 0
    def insert(self,data):
        if not self.head:
            self.head = Node(data)
            self.size += 1
        else:
            self._insert(data,self.head)

    def _insert(self,data,cur):
        if cur == data:
            cur.count += 1
            self.size += 1
            return 
        if data < cur:
            if cur.left != None:
                return self._insert(data,cur.left)
            else:
                new_node = Node(data)
                cur.left = new_node
                self.size += 1
        if data > cur:
            if cur.right != None:
                return self._insert(data,cur.right)
            else:
                new_node = Node(data)
                cur.right = new_node
                self.size += 1

    def remove(self,data):
        cur = self.head
        self._remove(data,cur)
    def _remove(self,data,cur):
        if data == cur:
            if cur.left and not cur.left.right:
                cur = cur.left
            elif cur.right and not cur.right.left:
                cur = cur.right
            
        else:
            self._remove(data,cur.left)
            self._remove(data,cur.right)
                
    def pprint(self,elem):
        if elem.left: self.pprint(elem.left)
        print "element:",elem,"count:",elem.count
        if elem.right: self.pprint(elem.right)
    
if __name__ == '__main__':
    import random
    bst = BinarySearchTree()
    for i in xrange(15): bst.insert(random.randint(0,1000))
    bst.pprint(bst.head)
    print bst.size
