__author__ = "Adam Najman"

"""
Adam Najman
CSCI HW 5
Dijkstra's Algorithm using an array!

Running time is O(V^2 + E)

Please see input.txt for graphs
The second to last graph has 12 nodes and 144 edges.
This takes twice as long in the array implementation
compared to the binary heap version.

"""




import re
from collections import defaultdict
from time import time

def dijkarray(v, ec):
  emat, cmat = [None for x in xrange(v)], \
               [float('inf') for y in xrange(v)]
  emat[0], cmat[0] = 0, 0
  source = min(ec.keys())
  rnd = ec[source]
  while rnd is not None and source < e:
    for elem in rnd:
      #print elem, source
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

  #print "v, e: ", v, e

  line = f.readline()
  #print "line: " , line
  delim = " ", "-", ":", "\n"
  pattern = '|'.join(map(re.escape, delim))

  foo = re.split(pattern, line)

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

  #t = time()
  ac = dijkarray(v, ec)
  print  ac
  #print t - time()



