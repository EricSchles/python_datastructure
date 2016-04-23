##Understanding Sort

Sorting algorithms are just as important as searching algorithms - and they are largely similar.  How you sort data is just as important as how you search data.  And both are reasonably hard to do efficiently.  But we can think of them both of classes of efficiency.  

Let's start off with the simiplest idea possible: bubble sort

The heart of our simple algorithms will be the following piece of code:

```
#assume a and b exist
tmp = a
a = b
b = tmp
```

This is the standard thing that happens in most text books when you swap the position of two variables.  However, python and other high level dynamic languages allow you to do this:


`a,b = b,a`

This is because we can treat b,a and a,b as tuples without the paranthesis.  And therfore we don't need the extra variable.  

Let's look at bubble sort now!

```
def bubble_sort(alist):
	for pass_through in xrange(len(alist)-1,0,-1):
		for current_index in xrange(len(alist[:pass_through+1])):
			if alist[current_index]>alist[current_index+1]:
				alist[current_index],alist[current_index+1] = alist[current_index+1],alist[current_index]
	return alist
```

The idea here is the most obvious (and overly simplistic) one possible - assuming any of the elements in the list are incorrectly ordered switch there position.  

So why do we have to do this in two for loops?  Because this switching: `a,b=b,a` only effects the current subset, but it may miss globally incorrectly sorted elements.  A very important distinction.  So we simply do it twice and all it a day.

A quick question for you - What is the running time of bubble sort?  

Best case is `O(n)`, because you have to go through the list at least once.  The worst case is `O(n^2)` because in the worst case - a completely unordered list you visit every element twice.  What's the space complexity? `O(1)` because you modify everything in place.  

Moving on!  Let's look at selection sort, which is a slight variation on this theme.  

Selection sort takes the idea of bubble sort: `a,b = b,a` and tries to improve on it, by only swapping out the largest element in the pass, instead of having to go through and swap every single one.  

```
def selection_sort(alist):
	for pass_through in xrange(len(alist)-1,0,-1):
		position_of_max = 0
		for current_index in xrange(1,len(alist[:pass_through+1])):
			if alist[current_index]>alist[position_of_max]:
				alist[current_index],alist[position_of_max]=alist[position_of_max],alist[current_index]
				position_of_max = current_index
	return alist
```

Finding the local max and then swaping that out guarantees will do less swaps, except when all the elements in the list are in reverse order.  So, what is the running time analysis for this algorithm?  

Well, best case is going to be `O(n^2)`, the average case is going to be `O(n^2)` and the worst case is going to be 
`O(n^2)`.  However, there will absolutely be fewer operations in selection sort than in bubble sort - so in benchmarks, selection sort runs faster!  Some times significantly.  

Up until now we've only looked at linear sorting algorithms - those that go through our list linearly.  This sort of looping should feel similar to how we did search - linearly walking through our list and interacting as needed.  However, in the case of sorting, "linear" operations have none linear run time complexity.  Which means, we are running in polynomial space.  This is no good!  Because as our array grows, we need twice as many operations to keep it ordered - a very important task for lots of real world applications.  So how might we get closer to keeping our list ordered in linear or better time?  Well, we might consider applying the same "technology" that we applied before - recursion.  A recursive algorithm in sorting land is referred to as divide and conquer, at least with arrays.  When we move onto graphs, it will be refered to in more nuianced terms.  

The first divide and conquer algorithm will look at is called merge sort - because we merge and sort elements.

The algorithm is actually pretty straight forward - break up our list into the smallest possible units in order and then merge them all back together. 

```
def merge_sort(alist):
	if len(alist) == 1:
		return alist
	mid = len(alist) // 2
	left = merge_sort(alist[:mid])
	right = merge_sort(alist[mid:])
	return merge(left,right)

def merge(left,right):
	merged = []
	left_ref, right_ref = 0,0
	while left_ref < len(left) and right_ref < len(right):
		if left[left_ref] < right[right_ref]:
			merged.append(left[left_ref])
			left_ref +=1
		else:
			merged.append(right[right_ref
	while left_ref < len(left):
		merged.append(left[left_ref])
	while right_ref < len(right):
		merged.append(right[right_ref])
	return merged
```

You might look at this set of operations and think to yourself, yuck!  That's a lot of code.  But don't worry it's there for good reason.  

It's hard to know how to start to write merge sort, but the basic idea is we start by splitting up our arrage, which is what happens in the merge_sort function:

```
def merge_sort(alist):
	if len(alist) == 1:
		return alist
	mid = len(alist)//2
	left = merge_sort(alist[:mid])
	right = merge_sort(alist[mid:])
	return merge(left,right)
```

What happens here is we recursively break up our list into lists of only one element.  Why recursively?  That's because then we can do it in only log n operations!  We implicitly exploit the structure of recursion here:

`left = merge_sort(alist[:mid])`

And here,

`right = merge_sort(alist[mid:])`

These two operations taken together we get to a binary tree!  Where `left`, is like the left reference in a binary tree node!  And `right` is like the right reference in a binary tree node.  Pretty nifty right?!

Once we have everything all split up we have to merge it back!  To do that we run iteratively through the two lists, joining together everything and making sure we do that in an ordered fashion.

So more or less what we are doing is comparing two lists - left and right and as long as the next element in left is less than the next element in right, append that one.  Otherwise we append the right element until we get to the next left element that is less than the right element.  After that we just append all the left array elements and then all the right array elements (because right should be more than left).  

Let's look at the code again for merge:

```
def merge(left,right):
	merged = []
	left_ref, right_ref = 0,0
	while left_ref < len(left) and right_ref < len(right):
		if left[left_ref] < right[right_ref]:
			merged.append(left[left_ref])
			left_ref +=1
		else:
			merged.append(right[right_ref
	while left_ref < len(left):
		merged.append(left[left_ref])
	while right_ref < len(right):
		merged.append(right[right_ref])
	return merged
```


After we do that we return the merged list up the recursive tree.  Then the recursion implicitly joins together the merged individual lists, forming one sorted list.  Notice that we impose an ordering to the elements of our split up arrays at every level, continually insuring that our final list will be ordered.  All and all this ads up over the breath and depth of the recursion.

So the recursive step gives ups `O(log n)` operations and the merge step gives us `O(n)` more operations.  Since we do `O(n)` operations inside of the recursive step we have to think of this as function composition and therefore our run times are multiplied.  So we end up with `O(n log n)` as our run time.  Which turns out to hold no matter how ordered or unordered our list.  You might think to yourself, boo!  But in fact `O(n log n)` is definitely an improvement over our previous algorithms - averaging `O(n^2)`.  And in the land of benchmarks this turns out to be a decent improvement. 

Now let's talk about quick sort - our first semi advanced algorithm.  Quick sort has a lot of different ways it can be implemented.  And some of them have lots and lots of pointer chasing.  Fortunately our version is very readible, in part due to the power of python's high level dynamic nature.  So without further ado, quick sort, written the right way:

```
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
```

The divide and conquer part of this algorithm occurs in the return statement.  Notice that we do divide and conquer here as well as in merge sort.  This algorithm works in a very simple way - the first element in the list is used as the pivot, anything less than this element is moved into a less array, anything equal is moved into an equal array, and anything greater is moved into a greater array.  Then the lists are concatenated.  During concatenation the ordering is applied.  Notice that we call quick_sort on less and that we have by design guaranteed that elements smaller than the current element will be in the less subarray.  The same holds true for greater.  Therefore all and all we end up with a loosely ordered set of lists that are recursively divided.  And then when each ordered singleton array is created, they are all joined.  

So how long does this take to run?  The answer is average `O(n log(n))`.  That's mostly because of the divide and conquer nature of the algorithm.  However quick sort has a worst case running time of `O(n^2)`.  


