"""
Adam Najman
nbest.py
Hw2
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

def nbestc(a):
  print a[-1]
  heapq.heapify(a)
  print a[-1]
  return

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
  
  return pivot, pivotSum, rest, left, right

def _qselect(a, b, c=[]):
  if a == []:
    return []
  
  pivot, pivotSum, rest, left, right = _part(a)
  left_size = len(left)

  while(len(c) < b):
    if left_size + 1 == b:
      left.append(a[pivot])
      c = left
      return c
    elif left_size >= b:
      a = left
      pivot, pivotSum, rest, left, right = _part(left)
      left_size = len(left)
    else:
      pivot, pivotSum, rest, left, right = _part(a)
      left_size = len(left)
  return c

n = 10
x = [random.randint(0,100) for _ in xrange(n)]
y = [random.randint(0,100) for _ in xrange(n)]

#x = [4,1,5,3]
#y = [2,6,3,4]

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
print "z.sort(): "
print z
print time.time()-t

print nbestc(z)

