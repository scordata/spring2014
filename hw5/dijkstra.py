import re
from collections import defaultdict

def dijkheap(e, ec):
  return None

def dijkarray(v, ec):
  emat, cmat = [None for x in xrange(v)], \
               [float('inf') for y in xrange(v)]
  emat[0], cmat[0] = 0, 0
  source = min(ec.keys())
  rnd = ec[source]
  while rnd is not None and source < e:
    for elem in rnd:
      print elem, source
      if elem[1] < cmat[elem[0]]:
        emat[elem[0]] = source
        cmat[elem[0]] = elem[1] + cmat[source]
    del ec[source]
    if len(ec.keys()) == 0:
      break
    source = min(ec.keys())
    rnd = ec[source]
  #print "emat is: ", emat #UNCOMMENT TO SEE TOTAL
  #print "cmat is: ", cmat #COSTS AND PATHS
  if cmat[-1] == float('inf'):
    return "UNREACHABLE"
  return cmat[-1]


f = open('input.txt', 'r')
v, e = 0, 0

while v is not -1:

  temp = f.readline()
  delim  = " "
  v, e = temp.split(delim)
  v, e = int(v), int(e)

  if v is -1:
    break

  print "v, e: ", v, e

  line = f.readline()
  print "line: " , line
  delim = " ", "-", ":", "\n"
  pattern = '|'.join(map(re.escape, delim))
  #print "pattern: " , pattern

  foo = re.split(pattern, line)
  #print "foo: ", foo
  """ 
  edges, costs = [], []
  c = 2

  for x in xrange(len(foo)-1):
    if x == c:
      costs.append(int(foo[c]))
      c += 3
      continue
    edges.append(int(foo[x]))

  print "edges: " , edges
  print "costs: " , costs
  """
  for x in xrange(len(foo)-1):
    foo[x] = int(foo[x])
  ec = defaultdict(list)
  qq = 0
  while qq < (len(foo)-1):
    if foo[qq] in ec.keys():
      temp = ec[foo[qq]]
      temp.append((foo[qq+1], foo[qq+2]))
      ec[foo[qq]] = temp
    else:
      ec[foo[qq]] = [(foo[qq+1], foo[qq+2])]
    qq += 3

  print "ec is: ", ec

  dijkheap(e, ec)
  ac = dijkarray(v, ec)
  print "array cost: " , ac



