import random
import time

def bubble_sort(alist):
    for pass_number in xrange(len(alist)-1,0,-1):
        for i in xrange(pass_number):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
    return alist
                
def selection_sort(alist):
    for fillslot in range(len(alist))[::-1]:
        positionOfMax=alist.index(max(alist[:fillslot+1]))
        alist[fillslot],alist[positionOfMax] = alist[positionOfMax],alist[fillslot]
    return alist


def merge_sort(alist):
    lefts = []
    rights = []
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return merge(left,right)

def merge2(left,right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:],right)
    return [right[0]] + merge(left,right[1:])

def merge(left,right):
    merged_array = []
    pointer_left,pointer_right = 0,0
    while pointer_left < len(left) and pointer_right < len(right):
        if left[pointer_left] < right[pointer_right]:
            merged_array.append(left[pointer_left])
            pointer_left += 1
        else:
            merged_array.append(right[pointer_right])
            pointer_right += 1
    while pointer_left < len(left):
        merged_array.append(left[pointer_left])
        pointer_left += 1
    while pointer_right < len(right):
        merged_array.append(right[pointer_right])
        pointer_right += 1
    return merged_array

def quick_sort(alist):
    less = []
    equal = []
    greater = []

    if len(alist) > 1:
        pivot = alist[0]
        for x in alist:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return alist
    
start = time.time()
alist = [random.randint(0,100000) for _ in xrange(2000)]
bubble_sort(alist[:])
print "bubble sort took",time.time() - start
start = time.time()
selection_sort(alist[:])
print "selection sort took",time.time() - start
start = time.time()
merge_sort(alist[:])
print "merge sort took",time.time() - start
start = time.time()
quick_sort(alist[:])
print "quick sort took",time.time() - start
