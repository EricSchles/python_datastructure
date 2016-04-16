def binary_search(elem,array,first,last):
    midpoint = (first + last) // 2
    print first,"first"
    print last,"last"
    if first > last:
        return -1
    if elem == array[midpoint]:
        return midpoint
    else:
        if elem < array[midpoint]:
            return binary_search(elem,array,first,midpoint-1)
        else:
            return binary_search(elem,array,midpoint+1,last)

def dyn_binary_search(elem,array):
    firsts = [0]
    lasts = [len(array)-1]
    while firsts[-1] <= lasts[-1]:
        midpoint = (firsts[-1] + lasts[-1]) // 2
        if elem == array[midpoint]:
            return midpoint
        elif elem < array[midpoint]:
            lasts.append(midpoint-1)
        else:
            firsts.append(midpoint+1)
    return -1
        
if __name__ == '__main__':
    import random
    import time
    size = 1000000
    listing = [random.randint(0,size) for i in xrange(size)]
    search_value = random.randint(0,size)
    listing.sort()
    start = time.time()
    binary_search_result =  binary_search(search_value,listing,0,len(listing)-1)
    binary_search_timing = time.time() - start
    print "binary search result:",binary_search_result,"and it took:",binary_search_timing
    try:
        listing.index(search_value)
        print "And the value actually exists"
    except:
        print "And the value doesn't actually exist"

        
