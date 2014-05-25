__author__ = "Adam Najman"

"""
Adam Najman
CSCI HW 5
Prim's Algorithm!

Running time is O(ElogV + VlogV) 

Please see input.txt for graphs.

This prints the very dense graph twice
as fast as Kruskal's


"""

import re
import heapq
from collections import defaultdict
from time import time

def prim(e, v, ec):
  nodes_left = e-1
  visited = set() #to check for cycles
  weight = 0
  edges = 0
  last_node = v-1
  retVal = []
  start = min(ec.keys())
  visited.add(start)


  while nodes_left > 0:

    pick = None

    #print "nodes_left", nodes_left
    nodes_left -= 1
    #print "visited: ", visited
    take = [float('inf'), float('inf')]
    for node in visited:
      #print "node: ", node
      #print "ec[node]: ", ec[node]
      if len(ec[node])  == 0:
        continue
      #print "min(ec[node]):", min(ec[node])
      if take > list(min(ec[node])):
        take = min(ec[node])
        pick = node
        foo = (node, take[1], take[0])

    if take == [float("inf"), float("inf")]:
      break
    
    retVal.append(foo)

    #print "take: ", take
    ec[pick].remove(take)
    #print "ec[node] after fix: ", ec[pick]
    weight += take[0]
    #print "weight: ", weight
    visited.add(take[1])

  if len(visited) < v:
    return 0, None


  return weight, retVal 

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
      temp.append((foo[qq+2], foo[qq+1]))
      ec[foo[qq]] = temp
    else:
      ec[foo[qq]] = [(foo[qq+2], foo[qq+1])]
    qq += 3
  #t = time()
  hc,p = prim(e, v, ec)
  #print "-----------------------------------"
  if hc == 0 and p is None:
    print "NO SPANNING TREE"
    continue

  print  hc,
  for zz in p:
    print "%i-%i:%i " % (zz[0],zz[1],zz[2]),
  #print t - time()
  print "\n"


