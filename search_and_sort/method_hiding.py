class List:
    def __init__(self):
        self.listing = []
    def append(self,data):
        self.listing.append(data)
    def remove(self,data):
        self.listing.remove(data)
    def get_element(self,index):
        return self.listing[index]
    def get_size(self):
        return len(self.listing)
    def pprint(self):
        print(self.listing)

if __name__ == '__main__':
    import random
    listing = List()
    [listing.append(random.randint(0,1000)) for _ in xrange(100)]
    first_elem = listing.get_element(0)
    listing.pprint()
    listing.remove(first_elem)
    listing.pprint()
