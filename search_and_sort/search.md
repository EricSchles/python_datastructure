##Understanding Search

The idea of search is pretty simple - find something you are looking for.  The simplest version of search exploits the ordering in ordered sets.  Thus if a set or list of objects is well ordered or an ordering can be imposed, then search is easy.  When there isn't an ordering or an obvious way to impose an ordering, search can be challenging, because an ordering must be imposed.  

##Simple Search

###Linear Search

Let's start with the classical version of search - linear search over the natural numbers.

```
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
```

This simple search function assumes two things - we are dealing with a single dimension list, which we will refer to as a simple list and we are dealing with the integers.  Of course, this search algorithm generalizes to any type of item.

Just for fun let's try a few examples:

```
>>> from search import linear_search as search
>>> search(5,[1,2,3,4])
-1
>>> search(5,[1,2,3,4,5])
4
>>> search(5,[1,2,5,4,5])
2
>>> search(5,[5,2,5,4,5])
0
>>> 
```

This shows that we'll always find the first occurence of the number 5.  Notice that we return the position position of the number if it exists instead of returning the number itself.  This is because we already know what we were looking for, so we merely want to know where it is, not what it is.

Next let's try to expand on our linear search, finding all the positions of the thing we were searching for.

```
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
```

Let's look at that example again:

```
>>> from search import linear_search_all_positions as search
>>> search(5,[1,2,3,4])
-1
>>> search(5,[1,2,3,4,5])
[4]
>>> search(5,[1,2,5,4,5])
[2, 4]
>>> search(5,[5,2,5,4,5])
[0, 2, 4]
>>> 
```

Great!  Now we get all the positions that we were looking for.  Let's try looking for all the characters in a string now.

```
>>> from search import linear_search as search
>>> search("a","abs")
0
>>> search("a","dbs")
-1
>>> search("a","cba")
2
>>> 
```

Look!  It works still.  This is because strings in Python are iterable.  In other languages this may not hold.  But you can always do a little extra work to make it work.

```
>>> search("hello",["hello","there","hello"])
0
>>> search("hello",["hi","there","hello"])
2
>>> 
```

And it even works over lists of words!

So as you can see, with the linear search algorithm we wrote, we can work on all data types that implement the equality operator.  Which means we can work over all classes of objects that implement this or have it implicitly implemented!!  And of course assuming we are working over a list.  

So what happens when we work over a different data type?  Like for instance a dictionary or a set.  Those are both iterable.  We may also want to work over more complex data structures like directed or undirected graphs.  

Let's save that for a little later on.  First let's see if we can do better than linear search.  

##Binary Search

So the answer in short is, yes we can do better than linear search, at least in terms of the number of operations.  This is generally referred to as big Oh notation.  The linear search algorithm will always perform in linear time - O(n), where n is the size of the object being searched.  Binary search, as we will see performs in O( log n ) time.  Meaning it will take at most log n operations to complete. However, this doesn't mean it will perform faster than linear search.  This is an implementation detail that has more to do with the underlying hardware and the lower level primitives, below the language layer.  

###Implementation

First let's look at binary search

```
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
```

There is slightly more going on here, so let's think through this a few lines at a time:

```
if not all([type(elem) == type(int()) for elem in listing]):
	raise Exception("Requires elements of type int!!!")
```

This ensures that all of the elements are of type integer and if they aren't raise an error.  

We are now ready to look at the meat of the code, almost.  First we must talk about about our assumption on the data.  We assume that our list is ordered in binary search.  If it wasn't then we couldn't use binary search.  This is a major distinction between linear search and binary search - linear search does not require an implicit ordering to work - it simply searches the whole space until the element is found.  For binary search we are in trouble if we can't order our elements or if some reason we are working over a non orderable set.  This will become clear as we look at the pieces of the algorithm, but it's important enough to mention that I am saying it up front.

```
found = False
first = 0
last = len(listing) - 1
```

Here we set up our system.  By setting the first to position 0 and the last to the last element of the list, we guarantee that the whole list will be checked - assuming it is well ordered.

```
while first < last:
```

Here we set the conditions under which our limit exits - a long as we haven't checked the whole list, which will be true as long as the first position we check doesn't equal the last position we check and as long as our element wasn't found.  If we found what we were looking for, of course we don't have to keep looking for it ;)

```
midpoint = (first + last) // 2
if listing[midpoint] == item:
    found = True
    break
```

Here we set up our midpoint - notice this is the only point we check and yet, this will find the item, if it's in the list with far fewer steps on average than linear search!!!!  However, these steps require more computation, so it's unclear which algorithm will be faster in practice.  

```
else:
    if first >= last:
        break
    else:
        if item < listing[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
```

We are now ready to look at the else block which gives us the rest of our logic.  So if the first element is greater than the last - then clearly we've checked our entire list, this will become clear when we look at the update logic:

```
if item < listing[midpoint]
```

This means that the item cannot be in a place greater than the current endpoint - so we set:

`last = midpoint - 1`

This means that we will now only search at point to the midpoint-1 element.  Or the left hand side from this point.  


`else:` - otherwise that means the item must be larger than the listing[midpoint] - which means we set the lowest possible value to `midpoint + 1`.  In this way we get O( log n).  That's because we have to do at most log base 2 n operations.  How can we see that?

Say we had the numers 1 - 100 and we were looking to see if 13 was in the list.  Here's how the algorithm would play out:

```
0th index first
99th index last
49th index midpoint

0th index first
48th index last
24th index midpoint

0th index first
23rd index last
11th index midpoint

12th index first
23rd index last
17th index midpoint

12th index first
16th index last
14th index midpoint

12th index first
13th index last
12th index midpoint

12th index is the answer
```

So let's count how many computations that took: 6 computations
If we did that with linear search it would have taken 12 computations to get to the 13th number.  That means we cut our cost in half!!!  Of course, the logic to process each round of the binary search is more expensive, so for very small n (say 100) linear search will outperform binary search.  But big-Oh notation looks at how things move asymptotically, not for some small number.  This is important for when you write code in the real world - sometimes linear is better - sometimes it's not.  It depends how much data you are working with and how much processing you will have to do!

Let's run some experiments to figure out when linear search loses to binary search in python on my computer :)

```
n = 1000
linear search result: 695 and it took: 8.39233398438e-05
binary search result: 695 and it took: 0.000255107879639
And the value actually exists
```

Okay, at 1000 linear search is still faster - let's go up to the next factor.

```
n = 10,000
linear search result: 5099 and it took: 0.000593185424805
binary search result: 5099 and it took: 0.00249195098877
And the value actually exists
```

Okay, looks like binary search is getting closer to linear search!  Let's crank it up!

```
n = 100,000
linear search result: -1 and it took: 0.0125389099121
binary search result: -1 and it took: 0.0261290073395
And the value doesn't actually exist
```

Looks like we have to keep going.

```
n = 1,000,000
linear search result: 572418 and it took: 0.109135866165
binary search result: 572419 and it took: 0.36368894577
And the value actually exists
``

```
n = 10,000,000
linear search result: -1 and it took: 2.09779405594
binary search result: -1 and it took: 3.68138289452
And the value doesn't actually exist
```

So what is the real take away here?  Asymptotics can take a long time to actually "get" there.  Which leads to an important question - Does big-oh matter?  Is it the right metric?  Perhaps not, but it's a way to think about code in the abstract - in fact it's one of the few ways to think about code in the abstract.  Because there isn't one language to rule them all and every single language implements primitives differently, it's next to impossible to say how long a given piece of code will perform.  And even after you get around the language ambiguity there is also the hardware ambiguity!  Specificially, the way a method is implemented in a high level language will compile down to machine code.  The underlying hardware however is what actually does all the work.  And depending on the hardware, the code will perform differently, with the same instructions.  You have to think of it this way - at the end of the day code is just the instructions of how to do something.  The physical thing doing the work is going to determine how fast or slow the work is accomplished.  

This particular thing can be hard to hear for a mid level programmer because they believe their code will run just fine on their machine.  But in reality, to make code run fast, you need a cluster of machines all working together, distributing out your code and then taking advantage of lots and lots of sophisticated networking primitives, concurrency, parallelism and other advanced scheduling techinques.

For the most part this is hidden from the programmer.  But sometimes, it matters a lot.

So, can we make our O( log n ) algorithm outperform our O(n) algorithm faster?  Sure we can!  To do that's introduce a concept called recursion:

Recursion works by employing functional programming as aposed to imperative programming.  The major staple of imperative programming is flow of control and looping.  Functional programming does away with loops and tries to minimize or do away with the use of state change in the function call.

Let's rewrite binary search as a recursive algorithm:

```
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
```

Look how much clear that is!  It does pretty much the same thing, but it's going to run faster now!!!

```
n = 1000
linear search result: 3776 and it took: 0.000440120697021
binary search result: 3776 and it took: 0.00255608558655
recursive binary search result: 3776 and it took: 1.90734863281e-05
And the value actually exists
```

Wow!  Recursive binary search blows linear and iterative binary search out of the water!!!! Now that's speed!!!  Okay, so that's pretty neat?  Can we do better?

Let's introduce a new concept, called dynamic programming.  That's where you replace the recursive calls with arrays.  Let's transform our recursive calls with arrays here:

```
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
```

Okay, so did we do any better?

Let's look at n = 1000 again:

```
linear search result: 1532 and it took: 0.000188827514648
binary search result: 1533 and it took: 0.00250101089478
recursive binary search result: 1533 and it took: 5.96046447754e-06
dynamic binary search result: 1533 and it took: 7.15255737305e-06
And the value actually exists
```

Well, we did almost as well `:P`.  Let's run a few more experiments!!

```
n = 10,000
linear search result: 8472 and it took: 0.00108885765076
binary search result: 8472 and it took: 0.0025839805603
recursive binary search result: 8472 and it took: 6.91413879395e-06
dynamic binary search result: 8472 and it took: 6.91413879395e-06
And the value actually exists
```

```
n = 100,000
linear search result: 1937 and it took: 0.000256061553955
binary search result: 1937 and it took: 0.00246500968933
recursive binary search result: 1937 and it took: 5.96046447754e-06
dynamic binary search result: 1937 and it took: 6.91413879395e-06
And the value actually exists
```

```
n = 1,000,000
linear search result: 1037 and it took: 0.000149011611938
binary search result: -1 and it took: 0.00320506095886
recursive binary search result: 1037 and it took: 8.10623168945e-06
dynamic binary search result: 1037 and it took: 1.00135803223e-05
And the value actually exists
```

Boom!  At a million function calls the dynamic code overtakes the recursive code by an order of magnitude!!! This may seem like an insignificant thing, but there are a lot of things you can expressive recursively and it's important to know that the dynamic method will almost always have better asymptotics.  We'll encounter this again and again in search problems that we tackle throughout.

Okay - so what is this topic really?  This is what is known as code refactoring - you write an approximate solution - the linear search method.  This is typically the simplest thing you can think of.  Then you have a good idea.  But it runs slow because it's been poorly implemented (our first attempt at binary search).  Then you use some fancy design pattern (aka recursion).  And then you use an even fancier technique (aka dynamic programming).  This is pretty much how software development goes - from prototype, to production.

So enough chat about "best practices".  Let's move onto something a little tougher!

##Bringing in Data Structures

So now we've seen some ways of accessing data from a python built-in data structure.  But what if you wanted to build that data structure yourself?  Well that's what we are going to be talking about in this section.  This will more or less be the data structure analog to the last section - we'll be covering linearly stored data and non-linearly or binarily stored data.

So let's get started!

###Enter the linked list

The linked list is probably the similest data structure you could think of.  There are a few ways implement it - wrap the builtin python list and just support a few operators.  This is a form of information hiding - only exposing the methods you want your user to have access to.  It's an important design principle and manifests in a few places - java code in large enterprise settings and in rest based api's with connections over a network.  Most coders not living in enterprise land will encounter rest based api's so that's the view we'll take.

So let's see how to wrap methods.  And then we'll interact over an api with our list.

```
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
```

As we can see, we wrap some of the methods of the builtin list and produce an "API" aka application programming interface into the builtin structure.  Why the heck might you want to do this in actual code?  Well, if you are working in Java land, this makes a lot of sense.  You might write a ton of internal methods that your client is never supposed to use because they mess up things if not called appropriately.  So by writing an "interface" class, the user will never access those methods.  Of course, hopefully we are adult enough at this point that if someone says don't do something in clearly written code, they just don't do it.  

Let's move onto an example that actually feels more relevant in 2016 - writing an api for a rest client.



Up until now we've dealt with one data structure - the list.  Now we are going to deal with an entirely different data structure - a tree.  It's worth noting that we've been implicitly dealing with tree data structures ever since we introduced recursion - because our function calls are carried out in a tree structure.  But now, we'll explicitly write down a tree data structure to deal with.

