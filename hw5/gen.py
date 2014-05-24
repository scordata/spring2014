from random import randint

o = open('graph.txt', 'w')

for x in xrange(12):
  for y in xrange(1, 12):
    s = "%i-%i:%i " % (x, y, randint(0,15))
    o.write(s)
