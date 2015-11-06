class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,index):
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index // 2 ]:
                tmp = self.heapList[index // 2]
                self.heapList[index // 2] = self.heapList[index]
                self.heapList[index] = tmp
            index //= 2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percDown(self,index):
        while (index * 2) <= self.currentSize:
            min_child = self.minChild(index)
            if self.heapList[index] > self.heapList[min_child]:
                tmp = self.heapList[index]
                self.heapList[index] = self.heapList[min_child]
                self.heapList[min_child] = tmp
            index = min_child

    def minChild(self,index):
        if index * 2 + 1 > self.currentSize:
            return index * 2
        else:
            if self.heapList[index*2] < self.heapList[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1

    def delMin(self):
        return_value = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return return_value

    def buildHeap(self,alist):
        index = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (index > 0):
            self.percDown(index)
            index -= 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
bh.insert(7)
for i in xrange(6): print(bh.delMin())
