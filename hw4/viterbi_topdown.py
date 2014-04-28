__author__ = "Adam Najman"

"""
Adam Najman
viterbi_topdown.py

A top-down (recursive) implementation of the general Viterbi
algorithm in python

"""


import sys
from collections import defaultdict
from collections import Counter

f = sys.stdin#open('input.txt', 'r')
o = open('output.txt', 'w')

num_graphs =  int(f.readline())

def viterbiTop(nodes, topo, graph, level=1, paths=0):
  #print "rec paths: ", paths
  level += 1
  #print "level: ", level
  #print "topo: ", topo
  #print "graph: ", graph
  #print "paths at level: ", graph[0]

  if level == nodes:
    return graph[0]

  paths += viterbiTop(nodes, topo[1:], graph[1:], level, graph[0]) 

  return paths


for times in xrange(num_graphs):
  path = 0
  temp = defaultdict(int)
  topograph = []
  line, line2 = f.readline(), f.readline()
  nodes, edges = int(line[0]), int(line[2])
  graph = [(int(line2[x+1]), int(line2[x+4])) for x, y in \
            enumerate(line2) if y == '(']
  graph2 = [edge[1] for edge in graph]

  testgraph = [ 0 for x in xrange(nodes)  ]

  for x, g in enumerate(graph):
    #print x, int(g[0])
    testgraph[g[0] - 1 ] += 1

  start, end = graph[0][0], nodes #graph[-1][0]
  print "nodes, edges: ", nodes, edges
  print "connections: ", line2 
  #print "graph: ", graph
  #print "graph2: ", graph2
  print "start node, end node: ", start, end
  #print "Indegree list : " , Counter(graph2)
  for x in xrange(edges):
    temp[graph[x][0]]
    temp[graph[x][1]] += 1
  #print "temp is: ", temp
  for v in temp:
    foo = min(temp, key=temp.get)
    #print "min temp is: ", foo
    topograph.append(foo)
    temp[foo] = float('inf')
    for z in graph:
      if z[0] == foo:
        if foo == end:
          #print "---------------------"
          break
        #print "con found: " , z
        temp[z[1]] -= 1
        path += 1
    #print "new temp: ", temp
    #print "path : ", path
  #if start not in temp:
  #  print "start node has indegree of 0"
  print "toposort was: ", topograph
  #print "number of paths: ", topograph.index(nodes)

  print "outdegree: ", testgraph
  if 0 not in testgraph:
    print "Graph #", times
    print "CYCLIC!"
    o.write("\nGraph #%i" % times)
    o.write("\nCYCLIC\n")
    continue

  print "Graph #", times
  o.write("Graph #%i\n" % times)
"""
  print "bottom up:"
  o.write("bottom up: ")

  foo = viterbiBot(nodes, topograph, testgraph)

  print "paths: ", foo
  o.write(str(foo))
"""
  print "topdown:"
  o.write("\ntopdown: ")

  bar = viterbiTop(nodes, topograph, testgraph)

  print "paths: ", bar
  o.write(str(bar))
  
  """
  matrix = [[0 for y in xrange(len(graph) + 1)] \
               for x in xrange(len(graph) + 1)]
  for elem in graph:
    matrix[elem[0]][elem[1]] = 1
  print "matrix: "
  for thing in matrix:
    print thing
  paths = []
  numpaths = 0
  for i in xrange(1, len(graph) + 1):
    if matrix[i][nodes] == 1:
      paths.append(i)
      numpaths += 1
  print paths
  print numpaths
  for j, h in enumerate(paths):
    print j, h
    if matrix[j][h] == 1:
      paths.append(j)
      print "HIT!", j, h
      numpaths += 1
  print paths
  print numpaths
  """
