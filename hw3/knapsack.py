__author__ = "Adam Najman"
__filename__ = "knapsack.py"
__homework_number__ = 3


"""
This has been significantly changed from the first
version as to model itself after the paradigm presented
in class. 

Strange bug that I can't catch in here:
  Bottom Up approch saves correct items, but is
  off by one on value totals
  Top Down approach saves correct value, but is
  off by one on item reconstruction....

1) If the Maximum Weight capacity is very high compared
    to the item set, the top-down approach is going to 
    be much faster. For example, with 7 types of items,
    ranging from 1-5 on weight, and a max Capacity of 
    22, the running time on bottom up was:
      -0.00086784362793
    and the number of non-zero cells was:
      307
    For top-down the running time was:
      -0.000582933425903
    and the number of non-zero cells was:
      38

2) With a very low weight capacity and very many items,
    the results will be reversed, for example with a 
    capacity of 3, and 140 items, the bottom up solution
    has 309 non-zero cells and the top down version has
    no non zero cells.

3) (Assuming I can squash the bug) This algorithm could 
    be tweaked to support real numbers, although it will
    require some precomputing on the input set. First, 
    find the the weight with the finest degree of 
    granularity, then multiply every weight (including
    the max capacity) by 10 * the granularity degree.
    For example, if every weight is measured to a tenth
    of a pound, but one is measured to a hundredth, then
    you must multiply all weights by 100.

"""

from collections import defaultdict
from time import time

def bottomup(items):
  # 2D dicts so we can use DP
  k = defaultdict(lambda: defaultdict(int))
  b = defaultdict(lambda: defaultdict(int))

  #for all weights
  for w in xrange(1, W):
    #cur = W-w
    #for all items
    for x in xrange(1, len(items)):
      #split into binary tree
      left = k[x-1][w]
      if w >= items[x][0]:
        right = k[x-1][w-items[x][0]] + items[x][1]
      else:
        right = float('-inf')
      
      #print "left is: ", left
      #print "right is: ", right

      if right > left:
        k[x][w] = right
        #construct DAG
        b[x][items[x][2]] += 1
      else:
        k[x][w] = left
        #b[x][items[x][2]] = False

      #k[w] = max(k[cur] + items[w][1], x)

  #print "k is: "
  #for x in k:
  #  print x, k[x]
  print "b is: "
  for x in b:
    print x, b[x]
  return k, b

def topdown(n, W):
  #memoize
  if W in opt[n]:
    return opt[n][W]
  #basecase
  if W == 0 or n == 0:
    opt[n][W] = 0
  else:
    #Recursivley split into b-tree
    left = topdown(n-1, W)
    if W >= items[n][0]:
      right = topdown(n-1, W-items[n][0]) + items[n][1]
    else:
      right = float('-inf')
    
    if right > left:
      opt[n][W] = right
      #build DAG
      back[n][items[n][2]] += 1
    else:
      opt[n][W] = left
      #back[n][W] = False
  #op[W-1] = max(topdown(op, n-1, W-1, items) \
  #          + items[n-1][1], n-1)
  #print "opt is: " , opt
  #print "back is: ", back

  return opt[n][W]

def output(val, trace):
  #max intervals to navigate best results
  idx =  max(val[max(val.keys())].values())
  dlim = trace[max(trace.keys())]

  o.write("%i \n" % idx)
  print "Max Val = " , idx

  print "dlim = " , dlim

  for x in xrange(n):
    #print "x is: ", x
    #print "dlim[x] is: ", dlim[x]
    if x not in dlim:
      o.write("0 ")
      print "0 "
    else:
      o.write("%i " % dlim[x])
      print dlim[x]
  o.write("\n---------------------\n")


items = []
f = open("input.txt", 'r')
o = open("output.txt", 'w')

for line in f:
  print line
  l = line.strip()
  items.append( map(int, l.split(' ')) )

print '-------------'
#Grab and store values
n = items[0][0]
W = items[0][1]
items = items[1:]
temp = []

#Make duplicate items to convert to 0-1
for i, x in enumerate(items):
  for y in xrange(x[2]):
    # (weight, value, item ID)
    new_item = (x[0], x[1], i)
    #print "TUPLE: ", new_item
    temp.append(new_item)

#print "temp is: ", temp
items = temp

print "n is %i" % n
print "W is %i" % W
print "items is: "
print items

t = time()
k, b = bottomup(items)
print "Bottom Up: ", t-time()
print '-------------'
idx =  max(k[max(k.keys())].values())


o.write("Bottom up solution: \n")
print "Bottom up solution"

output(k,b)
print "non-zero cells: "
print sum(len(d) for d in k.values())

o.write("Top Down Solution: \n")
print "Top Down Solution"

opt = defaultdict(lambda: defaultdict(int))
back = defaultdict(lambda: defaultdict(int))

t = time()
t1 =  topdown(len(items)-1, W)
print "Topdown: ", t-time()
print "non-zero cells: "
#print t1
#print "opt is: "
#for x in opt:
#  print x, opt[x]
#print "\nback is: "
#for x in back:
#  print x, back[x]
output(opt, back)
print sum(len(d) for d in opt.values())

#print btrace(n, W, b)
#print btrace(n, W, back)
