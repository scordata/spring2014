


f = open('input.txt', 'r')
o = open('output.txt', 'w')

np = "NOT POSSIBLE"


times = int(f.readline())

for x in xrange(times):
  hd, rd = {}, {}
  n, l = f.readline().split()
  n, l = int(n), int(l)
  print "Case #%i: " % int(x+1)
  print "n, l: ", n, l
  house = f.readline().split()
  print "house", house
  req = f.readline().split()
  print "req  ", req

  for a, h in enumerate(house):
    hd[h] = a
  for b, r in enumerate(req):
    rd[r] = b

  cc = 0
  ma = {}
  for r in req:
    if r in hd:
      cc += 1
      ma[r] =  hd[r]
  
  print "ma", ma
  if cc == n:
    print "Case #%i: %i" % (int(x+1), 0)
    continue


