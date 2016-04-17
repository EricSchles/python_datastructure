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
```

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

So rather than going through an entire discussion of the code, I'm only going to [reference it here](https://github.com/EricSchles/python_datastructure/tree/master/search_and_sort/api_stuff) and leave it to you to look at the boiler plate parts (__init__.py, init_db.py).

The files we care about are:

models.py, views.py, client.py

`models.py` sets up our abstraction around our data - which in this case is a linkedlist, modeled in our models.py (which informs the structure of our database).  Note that you can use references (which I'll explain in more detailed below) to model any data structure you might like in the database, at a high level of abstraction.  Databases themselves have their own internal data structures.  This vary in sophistication, one standard academic data structure used in databases is the b-tree, which we will also look at later.  For now, we take these abstractions as given and there exists some way to store data in our database and retrieve it.  And we can model any datastructure we like using our database.  (a question you may then ask yourself is, why study data structures at all? And instead just focus on the underlying algorithms, since that seems like the right way to think about things).  Don't worry I think this way too, but I digress.

Let's look at models.py to get a sense of how datastructure modeling occurs in the database:

```
from app import db

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.Integer)

    def __init__(self,data):
        self.data = data

    def __str__(self):
        return repr(self.data)
```

Pretty nice right?!  We have a performant version of our builtin python list, basically for free.  The trick is we need to either carry out computations on the database which limits our ability to debug.  Or we need to process our data in batches (called batch processing), reading little bits of our massive database into memory at time, so that we can store lots and lots of data.  

Let's break this down a little bit -

We can think of data in our database as more or less what data looks like in excel - there are rows and columns.  We have a single table in our database, where each row of our data has an id column and a data column.  The data column is the data in the database.  The id column is the "index" in our database.  This more or less gives us a list!  That's it :)

Now let's look at the client we are going to make to interact with our wrapper class!

`client.py`

```
import requests
import json
import random

print requests.post("http://localhost:5000/add", data = json.dumps({"data":"5"})).text
print requests.get("http://localhost:5000/size").text
print requests.post("http://localhost:5000/get_element", data = json.dumps({"data":"0"})).text
print requests.post("http://localhost:5000/pretty_print").text
print requests.post("http://localhost:5000/remove", data = json.dumps({"data":"5"})).text
```

So!  As you can see we can `add` data via the add route, we can check the size of our database - how much data is in it.  We can get individual elements, by index.  And we can remove data from our database.  Pretty awesome right!!!

This may not seem that impressive, until you realize this is happening over the network - therefore it's all happening between two different machines.  This is of course a simple example, but this framework extends to any type of distributed computation we may want to do.  And it's a precursor to thinking about cluster environments.

The last thing we need to look at is how we directly interact with our database.  This is all done in the controller - `views.py`:

```
from app import app
from flask import render_template,request
from app.models import Data
from app import db
import json

@app.route("/add",methods=["GET","POST"])
def add():
    dicter = json.loads(request.data)
    data = Data(int(dicter["data"]))
    db.session.add(data)
    db.session.commit()
    return "successfully added "+str(dicter["data"])
    
    
@app.route("/remove",methods=["GET","POST"])
def remove():
    dicter = json.loads(request.data)
    Data.query.filter_by(data=int(dicter["data"])).delete()
    return "successfully deleted "+str(dicter["data"])

@app.route("/size",methods=["GET","POST"])
def size():
    return str(Data.query.count())

@app.route("/get_element",methods=["GET","POST"])
def get_element():
    dicter = json.loads(request.data)
    return str([d.data for d in Data.query.filter_by(id=int(dicter["data"])).all()])

@app.route("/pretty_print",methods=["GET","POST"])
def pretty_print():
    return str([d.data for d in Data.query.all()])
```

I'm not going to dig too deep into the details here.  But I'll say you should check out the flask documentation, and flask-sqlalchemy to fully understand this code.

We've talked alittle bit about references, but we haven't formmally defined them yet.  

A reference is a typically used in the context of data.  We've actually been making use of references ever since we started programming:

say we have the value 5 and we want to capture this in to variables, x and y, like so:

```
x = 5
y = 5
```

In Python (and other dynamically typed scripting languages) everything is technically an object, so any assignment statement to a variable will be a reference to that object.  Here we reference x and y to the object 5.  

In this case, both x and y will allow you to access and make use of the "5 object" however you might normally use it. 

We can add x and y - `x + 5`, `x + y`, `5 + y`.

We can even reassign x or y or both to whatever we'd like:

```
y = 7
x = 4
```

We can even change the types, because python is a dynamic language and references are to objects, not specific types.

```
x = "hello"
y = "there"
```

It's a pretty big deal, and it's awesome.  So though we don't explicitly think of the assignment operator as creating a reference, it is!  And it allows us to do some pretty powerful high level things, in terms of expressability.  Creating the right references is hugely important and non-trivial (just try programming c++).  By not having to work directly with those, we can focus on the pieces that matter - making our algorithms correct.  

So now that you hopefully understand the idea of creating a reference (via assignment), let's so how it get's used to build data structures!

```
class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.prev = prev
        self.next = next
    #comparator methods
    def __lt__(self,other):
        return self.data < other
    def __gt__(self,other):
        return self.data > other
    def __eq__(self,other):
        return self.data == other
    def __ge__(self,other):
        return self.data >= other
    def __le__(self,other):
        return self.data <= other
    def __ne__(self,other):
        return self.data != other
    def __str__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur
        self.size += 1
        
    def get_element(self,index):
        if not index <= self.size: raise Exception("Index out of range")
        cur = self.head
        counter = 0
        while index != counter and index <= self.size:
            cur = cur.next
            counter += 1
        return cur.data
            
    def get_index(self,data):
        index = 0
        cur = self.head
        while cur:
            if cur == data:
                return index
            else:
                cur = cur.next
                index += 1
        return -1
            
    def remove(self,data):
        if not self.head: return
        if self.head == data:
            cur = self.head
            self.head = cur.next
            cur.next = None
            cur = None
            return
        cur = self.head
        while cur.next:
            if cur == data:
                prev_node = cur.prev
                new_next = cur.next
                prev_node.next = new_next
                new_next.prev = prev_node
                cur = None
                break
            cur = cur.next
        if cur == data:
            prev_node = cur.prev
            prev_node.next = None
            cur = None
            
    def pprint(self):
        if not self.head: print
        cur = self.head
        while cur:
            print cur,
            cur = cur.next
        print 
            
if __name__ == '__main__':
    import random
    ll = LinkedList()
    [ll.append(random.randint(0,1000)) for _ in xrange(10)]
    ll.pprint()
    element = ll.get_element(0)
    ll.remove(element)
    ll.pprint()
```

Let's start by looking at the node class:

```
class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.prev = prev
        self.next = next
    #comparator methods
    def __lt__(self,other):
        return self.data < other
    def __gt__(self,other):
        return self.data > other
    def __eq__(self,other):
        return self.data == other
    def __ge__(self,other):
        return self.data >= other
    def __le__(self,other):
        return self.data <= other
    def __ne__(self,other):
        return self.data != other
    def __str__(self):
        return repr(self.data)
```

All data structures are defined as a set of containers of data.  The way in which the containers or nodes are composed together determine the structure for the data, aka the data's structure.  The simplest possible structure for data is linear - a node connected only to one other node.  In this case we show a node that can connect both forward and backward - thus we have a linkedlist, where we can access elements before and after it only.  

The next and prev elements store references to the next node in the sequence and the previous node in the sequence.  That's all you can access in this way.  In this data structure - data is stored dynamically, at run time.  So there is no other way to know where in memory it will be, other than via referencing it.  

So how does referencing elements work?

Let's define a simpler node interface, for the purposes of understanding this:

```
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)

if __name__ == '__main__':
    head = Node(0)
    new_node = Node(1)
    head.next = new_node
    new_node = Node(2)
    head.next.next = new_node
    new_node = Node(3)
    head.next.next.next = new_node
    #Hopefully it's clear what I'm doing here - creating new nodes and then adding them to the linkedlist, not by name, but indirectly via node.next references.  Why do I need so many by new_node = Node(3)?  Because I've used up the previous references storing the previous nodes.
    #Now that I've done that, I'm ready to reference nodes via indirection!
    cur = head
    while cur:
        print cur
        cur = cur.next
```
This next way of making use of indirection is crucial to understanding referencing!  I set the cur - the current node, equal to the next object via `cur = cur.next`.  What this is saying is, I want to move forward to the next reference in the list of linked objects.  What else, might be weird is `while cur:`.  Since None is equal to False in Python and while loops end when they evaluate to False, we can make use of this.  In our `class Node` definition, we by default set the value of next to None, via `def __init__(self,data,next=None):`.  What this means is unless we explicitly set node.next to something else, it will be None.  So when we've reached the last node in our linked list of data, after that we automatically set cur = None (since eventually cur.next will be None).  And thus `cur` in `while cur:` evaluates to False eventually, ending the loop.  This coding pattern is very very hard to understand.  What you should do to convince yourself of how this works - 

try creating a bunch of nodes and try linking them.  Trying iterating through the linked elements and even try doing something more complex.  References can be one of the hardest conceptual barriers in computer science.  But once you can understand them, you can write any structure to your data you might like.  

And for those of you who are more mathematically minded, referencing is a precursor to understanding discrete sets, discrete structures and discrete topologies.  Using referencing you can create your own discrete topologies and thus model many types of mathematical systems!  You are guaranteed that your topologie will have a distance metric in fact!  Where distance will be defined by the number of vertices between A and B (for two nodes in the graph).  If none of that made sense, don't worry!  There are lots of good reasons to understand this for the less mathematically minded among us!

Now let's look at the linked list:

```
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur
        self.size += 1
        
    def get_element(self,index):
        if not index <= self.size: raise Exception("Index out of range")
        cur = self.head
        counter = 0
        while index != counter and index <= self.size:
            cur = cur.next
            counter += 1
        return cur.data
            
    def get_index(self,data):
        index = 0
        cur = self.head
        while cur:
            if cur == data:
                return index
            else:
                cur = cur.next
                index += 1
        return -1
            
    def remove(self,data):
        if not self.head: return
        if self.head == data:
            cur = self.head
            self.head = cur.next
            cur.next = None
            cur = None
            return
        cur = self.head
        while cur.next:
            if cur == data:
                prev_node = cur.prev
                new_next = cur.next
                prev_node.next = new_next
                new_next.prev = prev_node
                cur = None
                break
            cur = cur.next
        if cur == data:
            prev_node = cur.prev
            prev_node.next = None
            cur = None
            
    def pprint(self):
        if not self.head: print
        cur = self.head
        while cur:
            print cur,
            cur = cur.next
        print 
            
if __name__ == '__main__':
    import random
    ll = LinkedList()
    [ll.append(random.randint(0,1000)) for _ in xrange(10)]
    ll.pprint()
    element = ll.get_element(0)
    ll.remove(element)
    ll.pprint()
```

And let's first restrict ourselves to looking at just the append method and the __init__ method:

```
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur
        self.size += 1
```

This is technically all we need to create a linked list.  Everything else is more or less just me showing you what you can do, and showing off a little `:P`.

The __init__ method is very simple - we set the head of our linked list to be None at the start.  This is a choice and convention goes either way - so do what you think is easiest.  Some people like to put in a marker value called `"head"` into `self.head`.  It's honestly up to you.

I prefer to be a minimalist with my space.  And so I see such a value as excessive.  But again that is totally a taste thing.  

Let's move onto the append method - the heart of our linked list.  How you add data to a data structure determines it's data structure.  So whether it be an add, append, update, adjust, or however data is added to your data structure, that is where you should always look first to understand what your data structure is doing.  

As you can see from the append method, we take in data.  And then encapsulate it in a node.  In the simplest case - we simply set `self.head = Node(data)`.  Otherwise, we follow standard convention - setting up a reference node which will use to access different elements of the linkedlist.  While these elements are stored in `cur` we are free to manipulate them as we desire.  Since we are appending, elements should be added to the end of the linked list, which is why the statement:

```
while cur.next:
    cur = cur.next
```

is there.  This statement more or less says, while we are not at the last node in our linked list (because at the last node the next node after that will be None which is the same as False in a while loop), we update `cur` with the next node, `cur.next`.  If you are used to simply going to whatever element you want in an array, sorry!  That's not how this data structure works.  The reason arrays allow you to simply choose where in the list you want to go, is because they take advantage of certain properities of memory layout.  Specifically, they are stored in contigious blocks of memory - one piece of memory after another.  Since memory addresses are just numbers that are sequentially numbered, you can use simple addition (which is always a constant time operator) to get to the elements you care about.  So how might this look in an array versus a linked list?

say you have an array with for integers -

```
value address
1     1000
2     1004
3     1008
4     1012
```

Notice something about the addresses?  They are 4 address numbers away from each other!  Always!  This is because integers take up a fixed 4 bits.  So if we want the fourth element in our list, we simply need the address of the first element - `1000` and then we add `1000 + (3 places forward in memory ) * (4 bits each)` aka `1000 + 3*4`, which is `1012`.  And what do you know?!  That's exactly the address of the value 4.  

Unfortunately, linked lists are laid out with no such memory guarantee.  That's because they are dynamically assigned memory addresses from the program's memory heap, not the program's memory stack.  You don't need to understand the difference between these two in detail right now, except that heap addresses are random.  Where as stack addresses are sequential.  What's the advantage of pulling from one over the other?  Addresses in the heap may not be sequential but they are dynamic!  With arrays we need to know the size of the array ahead of time, which sucks!  With linked lists we can add new data or remove it as we please.  

So why are python builtin lists able to grow "dynamically"? Aren't they arrays?  Well they are, but they are objects, like everything else in Python.  So they aren't 'real' arrays.  But you don't have to worry about that!  If you were dealing with real arrays, you could just start with an array of a fixed size and then copy everything over to a larger array (say that's twice as big) everytime you run out of space.  This trick means that the size complexity is [memoized](https://en.wikipedia.org/wiki/Memoization).  I think it's out of scope to explain memoization but I'll link to the wikipedia article!  

SO! It's time for the secret sauce, assignment when we get to the right element:

```
new_node = Node(data) #this is creating the new node
cur.next = new_node #this is creating the reference and adding it to the linked lists
new_node.prev = cur #this is referencing back to the current element
```

Referencing back is going to make our lives a lot easier for removal of elements.  

Now let's look at remove
```
def remove(self,data):
    if not self.head: return
    if self.head == data:
        cur = self.head
        self.head = cur.next
        cur.next = None
        cur = None
        return
    cur = self.head
    while cur.next:
        if cur == data:
            prev_node = cur.prev
            new_next = cur.next
            prev_node.next = new_next
            new_next.prev = prev_node
            cur = None
            break
        cur = cur.next
    if cur == data:
        prev_node = cur.prev
        prev_node.next = None
        cur = None
```

`if self.head == data` - this statement means that the first element is the one we need to remove.  
`cur = self.head` - here we set up a reference to the node to be deleted.  
`self.head = cur.next` - here we set the new first node in the list equal to the second element of the list.
`cur.next = None` - here we delete the reference to the old second node.
`cur = None` - here we delete the current node, which is the old head node.

This handles the case when the head node is the one to be deleted.  In all other cases we need to iterate through the list, using linear search to find the correct element, assuming it exists in the list.  

```
cur = self.head
while cur.next:
    if cur == data:
        prev_node = cur.prev
        new_next = cur.next
        prev_node.next = new_next
        new_next.prev = prev_node
        cur = None
        break
    cur = cur.next  
```

specifically we use - `if cur == data:` to find the element.  

All the other logic is the same as before, except we make use of the previous element.  I'm going to leave it as an exercise to understand how we use new_next.prev, cur.prev, and prev_node `:)`.  

#Trees

Up until now we've dealt with one data structure - the list.  Now we are going to deal with an entirely different data structure - a tree.  It's worth noting that we've been implicitly dealing with tree data structures ever since we introduced recursion - because our function calls are carried out in a tree structure.  But now, we'll explicitly write down a tree data structure to deal with.

It's also worth noting that linear search and linked lists are analogs in the same way binary search and binary trees are analogs.  

