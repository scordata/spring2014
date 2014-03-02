"""
Test 1 
test1.py
Solution Attempts
Adam Najman
LAST EDIT: 2/5/14
"""
def _fib(n, cache):
  print "n is %i" % n
  if n in cache:
    print "n in cache"
    return cache[n]
  cache[n] = 1 if n < 2 else _fib(n-1, cache) + _fib(n-2, cache)
  return cache[n] 

def fib(n):
  return _fib(n, cache={})

def mergesorted(a,b):
  print "ms'd a"
  print a
  print "ms'd b"
  print b
  if a[-1] < b[-1]:
    print "len(a): %i" % len(a)
    print "len(b): %i" % len(b)
    print "returning: ",
    print a + b
    return 
  if a[0] < b[0]:
    print "second case"
    print "returning: ",
    print a + b
    return a + b
  print "third case"
  print "returning: ",
  print b + a
  return b + a
  
  return  

def mergesort(a):
  #print a
  if len(a) <= 1:
    return a
  left, right = mergesort(a[0:len(a)//2]), mergesort(a[len(a)//2:len(a)])
  #print left
  #print right
  return mergesorted(left, right)

foo = [5,6,4,7,3,8,2,9,1,0]
print mergesort(foo)
