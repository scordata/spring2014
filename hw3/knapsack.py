
def knapsack(max_weight, current, cache):
  if current < 0: 
    return 0, [0]

  temp = (max_weight, current)

  if temp in cache: 
    return cache[k]

  w, v, qty = items[current]
  values, keep = 0, [0]

  for x in xrange(1, qty):
    weight_dist = max_weight - x * w
    print "weight_dist is: ", weight_dist
    if weight_dist < 0: break

    val, taken = knapsack(weight_dist, current - 1, cache)

    if val + x * v > values:
      values = val + x * v
      keep = taken
      keep.append(x)

  cache[temp] = [values, keep]
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

t1, t2 = knapsack(W, len(items) - 1, {})
print "t1 is: ", t1
print "t2 is: ", t2

for thing in t2:
  o.write("%i " % thing)

