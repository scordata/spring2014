import re
import heapq
from collections import defaultdict

def dijkheap(v, ec):
  emat, cmat = [None for x in xrange(v)], \
               [float('inf') for y in xrange(v)]
  emat[0], cmat[0] = 0, 0
  h = []
  for k in ec.keys():
    heapq.heappush(h, (k, ec[k]))
  #print "heap: ", h
  while len(h) > 0:
    for elem in h[0][1]:
      #print elem, h[0]
      if elem[1] < cmat[elem[0]]:
        emat[elem[0]] = h[0][0]
        cmat[elem[0]] = elem[1] + cmat[h[0][0]]
    heapq.heappop(h)
    if len(h) == 0:
      break
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

  hc = dijkheap(v, ec)
  print  hc



