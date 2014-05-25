__author__ = "Adam Najman"

"""
Adam Najman
CSCI HW 5
Kruskal's Algorithm!

Running time is O(ElogE) 

Please see input.txt for graphs.

This prints the very sparse graph twice as 
fast and Prim's

"""

import re
import heapq
from collections import defaultdict
from time import time

def kruskal(e, v, graph):
  
  mst = []
  circle = set()
  weight = 0


  graph.sort(key=lambda cost: cost[2])

  for elem in graph:
    if elem[0] not in circle:
          #print "appending elem: ", elem
          mst.append(elem)
          weight += elem[2]
    circle.add(elem[0])

  #print mst, len(mst), weight
    
  if len(mst) < v-1:
    return mst, weight

  return mst, weight

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
  qq = 0
  graph = []
  while qq < (len(foo)-1):
    temp = (foo[qq], foo[qq+1], foo[qq+2])
    graph.append(temp)
    qq += 3
  #t = time()
  mst, weight = kruskal(e, v, graph)
  if weight == 0:
    print "NO SPANNING TREE"
    continue
  print weight,
  for elem in mst:
    print "%i-%i:%i " % (elem[0],elem[1],elem[2]),

  #print t - time()
  print "\n"


