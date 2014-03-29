__author__ = "Adam Najman"
__filename__ = "knapsack.py"
__homework_number__ = 3

from collections import defaultdict

def knapsack(max_weight, current, cache):
  #base case
  if current < 0: 
    return 0, [0]

  #tuple, since lists are unhashable
  temp = (max_weight, current)

  #cache to memoize previous results
  if temp in cache: 
    return cache[temp]

  #unpack vars so we can check
  wgt, vi, qty = items[current]
  #set counter vars
  values, keep = 0, [0]

  #begin "recursive loop"
  for x in xrange(1, qty):
    #calc weight left after adding this item
    weight_dist = max_weight - x * wgt
    #print "weight_dist is: ", weight_dist
    #break if we're out of room
    if weight_dist < 0:
      break
    #unpack subproblems into val and checked
    val, checked = knapsack(weight_dist, current - 1, cache)

    #If our new value is greater than the old one...
    if val + x * vi > values:
      #we can keep what we've checked
      keep = checked
      #add the current item
      keep.append(x)
      #update old value to new one
      values = val + x * vi

  #hash values
  cache[temp] = [values, keep]
  #return values and the item we're keeping
  return values, keep

items = []
f = open("input.txt", 'r')
o = open("output.txt", 'w')

for line in f:
  print line
  l = line.strip()
  items.append( map(int, l.split(' ')) )

print '-------------'

n = items[0][0]
W = items[0][1]
items = items[1:]

print "n is %i" % n
print "W is %i" % W
print "items is: "
print items
memo = {}
t1, t2 = knapsack(W, len(items) - 1, memo)
print "t1 is: ", t1
print "t2 is: ", t2

for thing in t2:
  o.write("%i " % thing)

#WORKING BOTTOM UP ALGO
#IMPLEMENT FILE IO
#Put into function
#Write top down
print '---------------------'
k = defaultdict(int)

for w in range(W-1):
  print "w", w
  print "W-w", W-w
  cur = W-w
  print "v: ", items[w][1]
  for x in range(n):
    k[w] = max(k[cur] + items[w][1], x)
    print k[w]

print '----------------------'
print k
print k.values()
print k.keys()
for x in k:
  if k[x] != 0:
    print x, k[x]

print max(k.values())
print '-----------------'

print "W is: ", W
op = defaultdict(int)
def topdown(op, n, W, items):
  print "op", op
  print "n", n
  print "W", W
  print "items[n-1][1]", items[n-1][1]
  if W == 0 or n == 0:
    print "returning"
    return 0
  op[W-1] = max(topdown(op, n-1, W-1, items) \
            + items[n-1][1], n-1)
  print op
  return 0

print topdown(op, n, W-1, items)
