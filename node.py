class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)

