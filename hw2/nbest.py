"""
Adam Najman
nbest.py
Hw2


Quicksort is O(n log n)

I've got a terrible bug with my implementation
of quickselect on this program. Try running this with
a value of n > 25. Sometimes with the default values
it will produce the right output, othertimes worng, 
and othertimes none at all. It tends to hang on large
output. I've tried to re-write it about a dozen times, 
with and without recursion, to no avail.

Since we're using a priority queue with Dijkstra's
it's going to be O(logn)

"""
import time
import random
import heapq

def nbesta(a,b):
  z = [(c,d) for c in a for d in b]
  nlist = _qsort(z)
  retVal = []
  for i in range(len(b)):
    retVal.append(nlist[i])
  return retVal

def nbestb(a,b):
  z = [(c,d) for c in a for d in b]
  nlist = _qselect(z, len(a))
  return nlist

def nbestc(a, b):
  if a == [] or b == []:
    return None
  heapq.heapify(a)
  heapq.heapify(b)

  z = [(c,d) for c in a for d in b]

  path, result =  build_path(z, z[0][0] + z[0][1])

  print path
  print result
    
# A form of Dijkstra's using a PQ  
def build_path(graph, source):
  retVal = []
  n = len(graph)/2

  PQ = [(0,source)]

  #Set everything to infinity
  distance = [float('inf') for x in range(n)]
  #Except the source node (0, in our case)
  distance[source] = 0


  #Iterate throught the queue...
  while len(PQ) != 0:
    (total, u) = heapq.heappop(PQ)
    
    for v in range(n):
      #print distance[v]
      #print graph[v]
      if distance[v] > distance[u] \
          + (graph[v][0] + graph[v][1]) :
        #Set new distane value for every unvisited node    
        distance[v] = distance[u] \
        + (graph[v][0] + graph[v][1])
        #Push visited nodes on queue
        heapq.heappush(PQ, (distance[v],v))
        #Grab their tuple value and append
        retVal.append(graph[v])

  return distance, retVal

def comp2(x,y,p,q):
  if ( (x + y) < (p + q) ) or \
      ( (x + y) == (p + q)  and \
      y < q):
        return -1
  if ( x + y ) > (p + q):
    return 1
  return 0

def comp(x,y,s):
  z = x[0] + x[1]
  if (z < s) or (z == s and x[1] < y[1]):
    return -1
  if z > s:
    return 1
  return 0


def _qsort(a):
  if a == []:
    return []

  pivot = a[0]
  pivotSum = pivot[0] + pivot[1]

  lesser = _qsort ( [(foo) for foo in a[1:] if 
                    comp(foo, pivot, pivotSum) < 0] ) 

  greater = _qsort( [ (foo) for foo in a[1:] if\
             comp(foo, pivot, pivotSum) >= 0] )

  return lesser + [pivot] + greater

def _part(a):
  pivot = random.randint(0, len(a)-1)
  pivotSum = a[pivot][0] + a[pivot][1]
  rest = a[:pivot] + a[pivot+1:]
  left, right = [], []
  for x in rest:
    if comp(x, a[pivot], pivotSum) < 0:
      left.append(x)
    else:
      right.append(x)
  
  return pivot, left, right

def _qselect(a, b, c=[]):
  if a == []:
    return []

  pivot, left, right = _part(a)
  
  leftSize = len(left)

  if leftSize  == b:
    return left
  elif leftSize > b:
    return _qselect(left, b)
  else:
    return _qselect(right, b-leftSize)
'''
  while(len(c) < b):
   # print b
   # print "left is:"
   # print left
   # print "a is:"
   # print a
   # print "right is:"
   # print right
    if len(a) == b:
      return a

    leftSize = len(left)

    if leftSize + 1 == b:
      left.append(a[pivot])
      return left
    elif leftSize >= b:
      a = left
      pivot, left, right = _part(left)
    else:
      print "road less taken"
      print len(right)
      c = left
      pivot, left, right = _part(right)
      left.append(c)
'''


n = 50
#x = [random.randint(0,100) for _ in xrange(n)]
#y = [random.randint(0,100) for _ in xrange(n)]

x = [4,1,5,3]
y = [2,6,3,4]

z = [(a,b) for a in x for b in y]

"""
print "x is: "
print x
print "y is: "
print y
print "z is: "
print z
"""

print "sort 1: "
t = time.time()
print nbesta(x,y)
print time.time() - t
print "sort 2: "
t = time.time()
print nbestb(x,y)
print time.time()-t
t = time.time()
#z.sort()
#print "z.sort(): "
#print z
#print time.time()-t

print nbestc(x,y)
print time.time()-t
