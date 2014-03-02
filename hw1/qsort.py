"""
  Adam Najman
  qsort.py
  Homework #1
  LAST EDIT: 1/29/14 
"""

def sort(a):
  """
  Function provided via slide
  """
  if a == []:
    return []
  else:
    pivot = a[0]
    left = [x for x in a if x < pivot ]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree):
  """
  Use of generators here
  to view the infix traversal, 
  this requires a cast to list
  following a print statement
  """
  if isinstance(tree, list):
    for x in tree:
      for y in sorted(x):
        yield y
  else:
    yield tree
    

def search(tree, x):
  """
  Basic search function
  relies on _search()
  """
  if _search(tree, x):
    return True
  return False

def insert(tree, x):
  temp = _search(tree, x)
  if not temp:
    """
    An emply list means you've
    found the pointer you're 
    looking for. Three appends
    to maintain structural integrity.
    """
    temp.append([])
    temp.append(x)
    temp.append([])

def _search(tree, x):
  """
  Binary search on the data structure
  built by the "buggy" quicksort code
    (Prefix traversal)
  """
  if tree == []:
   # print "Empty Tree / Not Found"
    return tree
  if x ==  tree[1]:
    return tree
  if x < tree[1]:
     return _search(tree[0], x)
  if x > tree[1]:
    return _search(tree[2], x)
  else:
    return -1

if __name__ == "__main__":
    foo = [4,2,6,3,5,7,1,9]
    print "list is: " 
    print foo
    print "sorting list..."
    foo = sort(foo)
    print "sorted list is: "
    print foo
    
    print "testing sorted(list)"
    print list(sorted(foo))
    
    print "searching for 3"
    print search(foo, 3)

    print "searching for 8"
    print search(foo, 8)

    print "testing _search(foo, 4)"
    print _search(foo, 4)

    print "testing _search(foo, 3)"
    print _search(foo, 3)

    print "testing _search(foo, 9)"
    print _search(foo, 9)

    print "testing _search(foo, 0)"
    print _search(foo, 0)

    print "testing _search(foo, 8)"
    print _search(foo, 8)

    print "_search(foo, 0) is _search(foo, 8)"
    print _search(foo, 0) is _search(foo, 8)

    print "inserting 3 into tree"
    insert(foo, 3)
    print foo

#    print "inserting 0 into tree:"
#    insert(foo, 0)
#    print foo
    
    print "inserting 6.5 into tree:"
    insert(foo, 6.5)
    print foo
