from linked_list_pure import LinkedList


def test_add_first():
    ll = LinkedList()
    ll.add_first(5)
    assert ll.contains(5) == True
    assert ll.at_index(5) == 0
    ll.add_first(6)
    assert ll.contains(6) == True
    assert ll.at_index(6) == 0

def test_add_at():
    ll = LinkedList()
    ll.add_at(5,0)
    assert ll.contains(5) == True
    assert ll.at_index(5) == 0
    ll_two = LinkedList([1,23,4,5,6,78])
    ll_two.add_at(12,0)
    assert ll_two.contains(12) == True
    assert ll_two.at_index(12) == 0
    ll_two.add_at(21,3)
    assert ll_two.contains(21) == True
    assert ll_two.at_index(21) == 3

def test_add_last():
    ll = LinkedList()
    ll.add_last(3)
    assert ll.contains(3) == True
    assert ll.at_index(3) == 0
    ll.add_last(4)
    assert ll.contains(4) == True
    assert ll.at_index(4) == 1
    ll.add_last(5)
    assert ll.contains(5)  == True
    assert ll.at_index(5) == 2

def test_remove_first():
    ll = LinkedList([1,2,3,4,5])
    ll.remove_first()
    assert ll.contains(1) == False
    assert ll.at_index(1) == False
    assert ll.length == 4
    ll = LinkedList([1])
    ll.remove_first()
    assert ll.length == 0
    assert ll.contains(1) == False
    assert ll.at_index(1) == False
    

def test_remove_last():
    ll = LinkedList([1,2,3,4,5])
    ll.remove_last()
    assert ll.contains(5) == False
    assert ll.at_index(5) == False
    assert ll.length == 4
    ll = LinkedList([1])
    ll.remove_last()
    assert ll.length == 0
    assert ll.contains(1) == False
    assert ll.at_index(1) == False

def test_clone():
    ll = LinkedList([1,2,3,4,5])
    ll_t = ll.clone()
    assert ll_t.contains(1) == True
    assert ll_t.contains(2) == True
    assert ll_t.contains(3) == True
    assert ll_t.contains(4) == True
    assert ll_t.contains(5) == True
    

def test_iterator():
    listing = [1,2,3,4,5]
    ll = LinkedList(listing)
    curr = ll.iterator()
    iterate = 0
    while curr != None:
        assert curr.item == listing[iterate]
        curr = curr.next
        iterate += 1


def test_peek():
    ll = LinkedList([1])
    assert ll.peek() == 1
    ll = LinkedList([2,1,3])
    assert ll.peek() == 2


def test_peek_last():
    ll = LinkedList([1,2,3])
    assert ll.peek_last() == 3
    ll = LinkedList([1])
    assert ll.peek_last() == 1


def test_remove():
    ll = LinkedList([1,2,3])
    ll.remove(1) 
    assert ll.contains(1) == False
    assert ll.contains(2) == True
    assert ll.contains(3) == True
    ll.remove(2)
    assert ll.contains(2) == False
    assert ll.contains(3) == True
    ll.remove(3)
    assert ll.contains(3) == False
    assert ll.remove(5) == False


def test_to_list():
    listing = [1,2,3,4]
    ll = LinkedList(listing)
    assert ll.to_list() == listing
    listing = [1]
    ll = LinkedList(listing)
    assert ll.to_list() == listing


