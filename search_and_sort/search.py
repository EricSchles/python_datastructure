def is_sorted(l):
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def recursive_binary_search(elem,array,first,last):
    midpoint = (first + last) // 2
    if first > last:
        return -1
    if elem == array[midpoint]:
        return midpoint
    else:
        if elem <= array[midpoint]:
            return recursive_binary_search(elem,array,first,midpoint-1)
        else:
            return recursive_binary_search(elem,array,midpoint+1,last)

def dyn_binary_search(elem,array):
    firsts = [0]
    lasts = [len(array)-1]
    while firsts[-1] <= lasts[-1]:
        midpoint = (firsts[-1] + lasts[-1]) // 2
        if elem == array[midpoint]:
            return midpoint
        elif elem <= array[midpoint]:
            lasts.append(midpoint-1)
        else:
            firsts.append(midpoint+1)
    return -1

def binary_search(item,listing):
    if not all([type(elem) == type(int()) for elem in listing]):
        raise Exception("Requires elements of type int!!!")
    found = False
    first = 0
    last = len(listing) - 1
    while first < last:
        midpoint = (first + last) // 2
        if listing[midpoint] == item:
            found = True
            break
        else:
            if first >= last:
                break
            else:
                if item < listing[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
    if found:
        return midpoint
    else:
        return -1
    
def linear_search(item,listing):
    position = 0
    found = False
    while position < len(listing) and not found:
        if listing[position] == item:
            found = True
            break
        position += 1
    if found:
        return position
    else:
        return -1

def linear_search_all_positions(item,listing):
    position = 0
    positions = []
    while position < len(listing):
        if listing[position] == item:
            positions.append(position)
        position += 1
    if positions:
        return positions
    else:
        return -1
    
if __name__ == '__main__':
    import random
    import time
    size = 10000
    listing = [random.randint(0,size) for i in xrange(size)]
    listing.sort()
    start = time.time()
    search_value = random.randint(0,size)
    linear_search_result = linear_search(search_value,listing)
    linear_search_timing = time.time() - start
    start = time.time()
    binary_search_result =  binary_search(search_value,listing)
    binary_search_timing = time.time() - start
    start = time.time()
    recursive_binary_search_result = recursive_binary_search(search_value,listing,0,len(listing)-1)
    recursive_binary_search_timing = time.time() - start
    start = time.time()
    dynamic_binary_search_result = dyn_binary_search(search_value,listing)
    dynamic_binary_search_timing = time.time() - start

    print "linear search result:",linear_search_result,"and it took:",linear_search_timing
    print "binary search result:",binary_search_result,"and it took:",binary_search_timing
    print "recursive binary search result:",recursive_binary_search_result,"and it took:",recursive_binary_search_timing
    print "dynamic binary search result:",dynamic_binary_search_result,"and it took:",dynamic_binary_search_timing
    try:
        listing.index(search_value)
        print "And the value actually exists"
    except:
        print "And the value doesn't actually exist"
    
