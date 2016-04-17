class Node:
    def __init__(self,data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self,other):
        return self.data < other
    def __gt__(self,other):
        return self.data > other
    def __le__(self,other):
        return self.data <= other
    def __ge__(self,other):
        return self.data >= other
    def __eq__(self,other):
        return self.data == other
    def __ne__(self,other):
        return self.data != other
    def __str__(self):
        return repr(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data,self.root)     
    def _insert(self,data,cur):
        if data < cur:
            if not cur.left: cur.left = Node(data)
            else: self._insert(data,cur.left)
        else:
            if not cur.right: cur.right = Node(data)
            else: self._insert(data,cur.right)
            
    def pprint(self):
        if not self.root: return
        self._pprint(self.root,0)
    def _pprint(self,cur,level):
        print level*"*"+str(cur),
        if cur.left:self._pprint(cur.left,level+1)
        if cur.right:self._pprint(cur.right,level+1)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.insert(1)
    bst.insert(9)
    bst.pprint()
