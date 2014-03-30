__author__ = "Adam Najman"
__filename__ = "knapsack.py"
__homework_number__ = 3

from collections import defaultdict

def bottomup(items):
  k = defaultdict(int)

  for w in range(W-1):
    cur = W-w
    for x in range(n):
      k[w] = max(k[cur] + items[w][1], x)

  return k

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

k = bottomup(items)

o.write("%i \n" % max(k.values()))

for thing in k:
   if k[thing] != 0:
    o.write("%i " % thing)


print "W is: ", W
op = defaultdict(int)
def topdown(op, n, W, items):
  if W == 0 or n == 0:
    return 0
  op[W-1] = max(topdown(op, n-1, W-1, items) \
            + items[n-1][1], n-1)
  print op
  return 0

print topdown(op, n, W-1, items)
