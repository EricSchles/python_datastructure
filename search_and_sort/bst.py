class Node:
    def __init__(self,data,left=None,right=None,parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent
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
        if not self.root:self.root = Node(data)
        else:self._insert(data,self.root)
        self.size += 1
    def _insert(self,data,cur):
        if data < cur:
            if not cur.left:
                new_node = Node(data)
                cur.left = new_node
                new_node.parent = cur
            else: self._insert(data,cur.left)
        else:
            if not cur.right:
                new_node = Node(data)
                cur.right = new_node
                new_node.parent = cur
            else: self._insert(data,cur.right)
            
    def pprint(self):
        if not self.root: return
        self._pprint(self.root,0)
    def _pprint(self,cur,level):
        print level*"*"+str(cur)
        if cur.left:self._pprint(cur.left,level+1)
        if cur.right:self._pprint(cur.right,level+1)

    def exists(self,data):
        cur = self.root
        return self._exists(data,cur)
    def _exists(self,data,cur):
        if data == cur:return True
        elif data < cur:
            if cur.left:return self._exists(data,cur.left)
            else: return False
        else:
            if cur.right: return self._exists(data,cur.right)
            else: return False

    def get(self,data):
        cur = self.root
        return self._get(data,cur)
    def _get(self,data,cur):
        if data == cur: return cur
        elif data < cur:
            if cur.left: return self._get(data,cur.left)
            else: return False
        else:
            if cur.right: return self._get(data,cur.right)
            else: return False

    def children_count(self,cur):
        count = 0
        if cur.left: count += 1
        if cur.right: count += 1
        return count
    
    def delete(self,data):
        cur = self.get(data)
        if cur:
            num_children = self.children_count(cur)
            parent = cur.parent
            if num_children == 0:
                if parent:
                    if parent.left is cur: parent.left = None
                    elif parent.right is cur: parent.right = None
                elif cur is self.root:
                    self.root = None
            elif num_children == 1:
                if cur.left:
                    new_node = cur.left
                    new_node.parent = cur.parent
                else:
                    new_node = cur.right
                    new_node.parent = cur.parent
                if parent:
                    if parent.left is cur:
                        parent.left = None
                        cur = None
                        parent.left = new_node
                    elif parent.right is cur:
                        parent.right = None
                        cur = None
                        parent.right = new_node
                else:
                    self.root = None
                    cur = None
                    self.root = new_node
            else:
                parent = cur
                successor = cur.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                cur.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
        self.size -= 1
        
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.insert(1)
    bst.insert(9)

    bst.pprint()
    
    bst.delete(7)
    bst.delete(1)
    bst.delete(3)
    bst.delete(9)
    bst.delete(5)

    
    bst.pprint()
